"""
 m3ufu
"""

import json
import sys
import threefive
from new_reader import reader

"""
Odd number versions are releases.
Even number versions are testing builds between releases.

Used to set version in setup.py
and as an easy way to check which
version you have installed.
"""

MAJOR = "0"
MINOR = "0"
MAINTAINENCE = "39"


def version():
    """
    version prints the m3ufu version as a string
    """
    return f"{MAJOR}.{MINOR}.{MAINTAINENCE}"


def version_number():
    """
    version_number returns version as an int.
    if version() returns 2.3.01
    version_number will return 2301
    """
    return int(f"{MAJOR}{MINOR}{MAINTAINENCE}")


BASIC_TAGS = (
    "#EXTM3U",
    "#EXT-X-VERSION",
)

MULTI_TAGS = (
    "#EXT-X-INDEPENDENT-SEGMENTS",
    "#EXT-X-START",
    "#EXT-X-DEFINE",
)

MEDIA_TAGS = (
    "#EXT-X-TARGETDURATION",
    "#EXT-X-MEDIA-SEQUENCE",
    "#EXT-X-DISCONTINUITY-SEQUENCE",
    "#EXT-X-PLAYLIST-TYPE",
    "#EXT-X-I-FRAMES-ONLY",
    "#EXT-X-PART-INF",
    "EXT-X-SERVER-CONTROL",
)

SEGMENT_TAGS = (
    "#EXT-X-PUBLISHED-TIME",
    "#EXT-X-PROGRAM-DATE-TIME",
)

HEADER_TAGS = BASIC_TAGS + MULTI_TAGS + MEDIA_TAGS + SEGMENT_TAGS


class TagParser:
    """
    TagParser parses all HLS Tags as of the latest RFC.
    Custom tags will also be parsed if possible.
    Parsed tags are stored in the Dict TagParser.tags.
    TagParser is used by the Segment class.

    Example 1:

        #EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=2030321,BANDWIDTH=2127786,CODECS="avc1.4D401F,mp4a.40.2",RESOLUTION=768x432,CLOSED-CAPTIONS="text"

                TagParser.tags["#EXT-X-STREAM-INF"]= {"CLOSED-CAPTIONS": "text",
                                                        "RESOLUTION": "768x432",
                                                        "CODECS": "avc1.4D401F,mp4a.40.2",
                                                        "BANDWIDTH": 2127786,
                                                        "AVERAGE-BANDWIDTH": 2030321}

    Example 2:

        #EXT-X-CUE-OUT-CONT:ElapsedTime=21.000,Duration=30,SCTE35=/DAnAAAAAAAAAP/wBQb+AGb/MAARAg9DVUVJAAAAAn+HCQA0AALMua1L

                TagParser.tags["#EXT-X-CUE-OUT-CONT"] = {"SCTE35": "/DAnAAAAAAAAAP/wBQb+AGb/MAARAg9DVUVJAAAAAn+HCQA0AALMua1L",
                                                        "Duration": 30,
                                                        "ElapsedTime": 21.0}
    """

    def __init__(self, lines=None):
        self.tags = {}
        for line in lines:
            self._parse_tags(line)

    @staticmethod
    def atoif(value):
        """
        atoif converts ascii to (int|float)
        """
        if "." in value:
            try:
                value = float(value)
            finally:
                return value
        else:
            try:
                value = int(value)
            finally:
                return value

    @staticmethod
    def _strip_last_comma(tail):
        if tail.endswith(","):
            tail = tail[:-1]
        return tail

    def _parse_tags(self, line):
        """
        _parse_tags parses tags and
        associated attributes
        """
        line = line.replace(" ", "")
        if ":" not in line:
            return
        tag, tail = line.split(":", 1)
        self.tags[tag] = {}
        self._split_tail(tag, tail)

    def _split_tail(self, tag, tail):
        """
        _split_tail splits key=value pairs from tail.
        """
        while tail:
            tail = self._strip_last_comma(tail)
            if "=" not in tail:
                self.tags[tag] = self.atoif(tail)
                return
            tail, value = self._split_value(tag, tail)
            tail = self._split_key(tail, tag, value)
            if not tail:
                return

    def _split_key(self, tail, tag, value):
        """
        _split_key splits off the last attribute key
        """
        if tail:
            splitup = tail.rsplit(",", 1)
            if len(splitup) == 2:
                tail, key = splitup
            else:
                key = splitup[0]
                tail = None
            self.tags[tag][key] = value
        return tail

    def _split_value(self, tag, tail):
        """
        _split_value does a right split
        off tail for the value in a key=value pair.
        """
        if tail[-1:] == '"':
            tail, value = self._quoted(tag, tail)
        else:
            tail, value = self._unquoted(tag, tail)
        return tail, value

    def _quoted(self, tag, tail):
        """
        _quoted handles quoted attributes
        """
        value = None
        try:
            tail, value = tail[:-1].rsplit('="', 1)
        except:
            self.tags[tag]
            value = tail.replace('"', "")
            tail = None
        return tail, value

    def _unquoted(self, tag, tail):
        """
        _unquoted handles unquoted attributes
        """
        value = None
        try:
            tail, value = tail.rsplit("=", 1)
            value = self.atoif(value)
        except:
            tail = None
        return tail, value


class Segment:
    """
    The Segment class represents a segment
    and associated data
    """

    def __init__(self, lines, media_uri, start):
        self._lines = lines
        self.media = media_uri
        self.pts = None
        self.start = start
        self.end = None
        self.duration = 0
        self.cue = False
        self.cue_data = None
        self.tags = {}

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def _dot_dot(media_uri):
        """
        dot dot resolves '..' in  urls
        """
        ssu = media_uri.split("/")
        ss, u = ssu[:-1], ssu[-1:]
        while ".." in ss:
            i = ss.index("..")
            del ss[i]
            del ss[i - 1]
        media_uri = "/".join(ss + u)
        return media_uri

    def kv_clean(self):
        """
        _kv_clean removes items from a dict if the value is None
        """

        def b2l(val):
            if isinstance(val, (list)):
                val = [b2l(v) for v in val]
            if isinstance(val, (dict)):
                val = {k: b2l(v) for k, v in val.items()}
            return val

        return {k: b2l(v) for k, v in vars(self).items() if v}

    def _get_pts_start(self, seg):
        if not self.start:
            pts_start = 0.000000
            try:
                strm = threefive.Stream(seg)
                strm.decode(func=None)
                if len(strm.start.values()) > 0:
                    pts_start = strm.start.popitem()[1]
                self.start = self.pts = round(pts_start / 90000.0, 6)
            except:
                pass
        self.start = self.pts

    def _extinf(self):
        if "#EXTINF" in self.tags:
            self.duration = round(float(self.tags["#EXTINF"]), 6)

    def _scte35(self):
        if "#EXT-X-SCTE35" in self.tags:
            self.cue = self.tags["#EXT-X-SCTE35"]["CUE"]
            #  if "CUE-OUT" in self.tags["#EXT-X-SCTE35"]:
            #     if self.tags["#EXT-X-SCTE35"]["CUE-OUT"] == "YES":
            self._do_cue()
            #  if "#EXT-X-CUE-OUT" in self.tags:
            #     self._do_cue()
            return
        if "#EXT-X-DATERANGE" in self.tags:
            if "SCTE35-OUT" in self.tags["#EXT-X-DATERANGE"]:
                self.cue = self.tags["#EXT-X-DATERANGE"]["SCTE35-OUT"]
                self._do_cue()
                return
        if "#EXT-OATCLS-SCTE35" in self.tags:
            self.cue = self.tags["#EXT-OATCLS-SCTE35"]
            if isinstance(self.cue,dict):
                self.cue = self.cue.popitem()[0]
            self._do_cue()
            return
        if "#EXT-X-CUE-OUT-CONT" in self.tags:
            try:
                self.cue = self.tags["#EXT-X-CUE-OUT-CONT"]["SCTE35"]
            finally:
                return

    def show(self):
        """
        show prints the segment data as json
        """
        print(json.dumps(self.kv_clean(), indent=4))

    def _do_cue(self):
        """
        _do_cue parses a SCTE-35 encoded string
        via the threefive.Cue class
        """
        if self.cue:
            print(self.cue)
            try:
                tf = threefive.Cue(self.cue)
                tf.decode()
                self.cue_data = tf.get()
            except:
                pass

    def decode(self):
        # self.media = self._dot_dot(self.media)
        self.tags = TagParser(self._lines).tags
        self._extinf()
        self._scte35()
        if not self.start:
            self._get_pts_start(self.media)
            self.start = self.pts
        if not self.start:
            self.start = 0.0
        self.start = round(self.start, 6)
        self.end = round(self.start + self.duration, 6)
        del self._lines
        return self.start


class M3uFu:
    """
    M3u8 parser.
    """

    def __init__(self, arg):
        self.m3u8 = arg
        self.hls_time = 0.0
        self.media_list = []
        self._start = None
        self.chunk = []
        self.base_uri = ""
        if arg.startswith("http"):
            based = arg.rsplit("/", 1)
            if len(based) > 1:
                self.base_uri = f"{based[0]}/"
        self.manifest = None
        self.segments = []
        self.next_expected = 0
        self.master = False
        self.reload = True
        self.headers = {}

    @staticmethod
    def _clean_line(line):
        if isinstance(line, bytes):
            line = line.decode(errors="ignore")
            line = line.replace("\n", "").replace("\r", "")
        return line

    def _is_master(self, line):
        playlist = False
        if "STREAM-INF" in line:
            self.master = True
            self.reload = False
            if "URI" in line:
                playlist = line.split('URI="')[1].split('"')[0]
        return playlist

    def _set_times(self, segment):
        if not self._start:
            self._start = segment.start
        self._start += segment.duration
        self.next_expected = self._start + self.hls_time
        self.next_expected += round(segment.duration, 6)
        self.hls_time += segment.duration

    def _add_media(self, media):
        if media not in self.media_list:
            self.media_list.append(media)
            self.media_list = self.media_list[-200:]
            segment = Segment(self.chunk, media, self._start)
            self.segments.append(segment)
            segment.decode()
            self._set_times(segment)

    def _do_media(self, line):
        media = line
        if not line.startswith("http"):
            media = self.base_uri + media
        playlist = self._is_master(line)
        if playlist:
            media = playlist
        self._add_media(media)
        self.chunk = []

    def _parse_header(self, line):
        splitline = line.split(":", 1)
        if splitline[0] in HEADER_TAGS:
            val = ""
            tag = splitline[0]
            if len(splitline) > 1:
                val = splitline[1]
            self.headers[tag] = val
            return True
        return False

    def _parse_line(self):
        line = self.manifest.readline()
        if not line:
            return False
        line = self._clean_line(line)
        if "ENDLIST" in line:
            self.reload = False
        if not self._parse_header(line):
            self._is_master(line)
            self.chunk.append(line)
            if not line.startswith("#") or line.startswith("#EXT-X-I-FRAME-STREAM-INF"):
                if len(line):
                    self._do_media(line)
        return True

    def decode(self):
        while self.reload:
            with reader(self.m3u8) as self.manifest:
                while self.manifest:
                    if not self._parse_line():
                        break
                jason = {
                    "headers": self.headers,
                    "media": [seg.kv_clean() for seg in self.segments],
                }
                print(json.dumps(jason, indent=4))


if __name__ == "__main__":
    args = sys.argv[1:]
    for arg in args:
        fu = M3uFu(arg)
        fu.decode()
