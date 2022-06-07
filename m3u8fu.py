"""
 m3u8fu
"""

import json
import sys
import threefive


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
    version prints threefives version as a string
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

    def _quoted(self, tag, tail):
        """
        _quoted handles quoted attributes
        """
        value = None
        try:
            tail, value = tail[:-1].rsplit('="', 1)
        except:
            self.tags[tag] = tail.replace('"', "")
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

    def __init__(self, lines=None):
        self.tags = {}
        for line in lines:
            self._parse_tags(line)


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
            if "CUE-OUT" in self.tags["#EXT-X-SCTE35"]:
                if self.tags["#EXT-X-SCTE35"]["CUE-OUT"]=="YES":
                    self._do_cue()
            return
        if "#EXT-OATCLS-SCTE35" in self.tags:
            self.cue = self.tags["#EXT-OATCLS-SCTE35"]
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
            tf = threefive.Cue(self.cue)
            tf.decode()
            self.cue_data = tf.get()

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


class M3U8fu:
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
        if "STREAM-INF" in line:
            self.master = True
            self.reload = False

    def _do_media(self, line):
        media = line
        if self.master and "URI" in line:
            media = line.split('URI="')[1].split('"')[0]
        if not line.startswith("http"):
            media = self.base_uri + media
        if media not in self.media_list:
            self.media_list.append(media)
            self.media_list = self.media_list[-200:]
            segment = Segment(self.chunk, media, self._start)
            self.segments.append(segment)
            segment.decode()
            if not self._start:
                self._start = segment.start
            self._start += segment.duration
            self.next_expected = self._start + self.hls_time
            self.next_expected += round(segment.duration, 6)
            self.hls_time += segment.duration

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

    def _parse_line(self, line):
        self._is_master(line)
        self.chunk.append(line)
        if not line.startswith("#") or line.startswith("#EXT-X-I-FRAME-STREAM-INF"):
            if len(line):
                self._do_media(line)

    def decode(self):
        while self.reload:
            with threefive.reader(self.m3u8) as self.manifest:
                while self.manifest:
                    line = self.manifest.readline()
                    if not line:
                        break
                    line = self._clean_line(line)
                    if not self._parse_header(line):
                        self._parse_line(line)
                    if "ENDLIST" in line:
                        self.reload = False
                jason ={"headers":self.headers,
                        "media":[seg.kv_clean() for seg in self.segments]}
                print(json.dumps(jason, indent=4))
                return jason


if __name__ == "__main__":
    args = sys.argv[1:]
    for arg in args:
        fu = M3U8fu(arg)
        fu.decode()
