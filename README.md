# hls
M3U8 Parser with full SCTE-35 Support
![image](https://user-images.githubusercontent.com/52701496/169634298-5d7cdf40-87f6-42be-94f1-e14fbf6b2566.png)
...
![image](https://user-images.githubusercontent.com/52701496/169634341-1c4e1898-3a0f-493b-9e61-1aea24faf5ea.png)
...
![image](https://user-images.githubusercontent.com/52701496/169634383-a4b2bd24-3329-46ad-9517-a291dd85e71c.png)


```smalltalk
#EXTM3U
#EXT-X-INDEPENDENT-SEGMENTS

#EXT-X-VERSION:7
#EXT-X-MEDIA:TYPE=CLOSED-CAPTIONS,INSTREAM-ID="CC1",GROUP-ID="text",NAME="CC1",LANGUAGE="en",DEFAULT=YES,AUTOSELECT=YES

#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=2030321,BANDWIDTH=2127786,CODECS="avc1.4D401F,mp4a.40.2",RESOLUTION=768x432,CLOSED-CAPTIONS="text"
media-4/stream.m3u8
#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=393177,BANDWIDTH=410181,CODECS="avc1.4D400D,mp4a.40.2",RESOLUTION=416x234,CLOSED-CAPTIONS="text"
media-1/stream.m3u8
#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=698361,BANDWIDTH=727459,CODECS="avc1.4D400D,mp4a.40.2",RESOLUTION=416x234,CLOSED-CAPTIONS="text"
media-2/stream.m3u8
#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=1210676,BANDWIDTH=1263349,CODECS="avc1.4D401E,mp4a.40.2",RESOLUTION=640x360,CLOSED-CAPTIONS="text"
media-3/stream.m3u8
#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=2748961,BANDWIDTH=2913843,CODECS="avc1.4D401F,mp4a.40.2",RESOLUTION=960x540,CLOSED-CAPTIONS="text"
media-5/stream.m3u8
#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=5312128,BANDWIDTH=5652395,CODECS="avc1.4D401F,mp4a.40.2",RESOLUTION=1280x720,CLOSED-CAPTIONS="text"
media-6/stream.m3u8
#EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=8391745,BANDWIDTH=8963399,CODECS="avc1.640028,mp4a.40.2",RESOLUTION=1920x1080,CLOSED-CAPTIONS="text"
media-7/stream.m3u8

#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=64059,BANDWIDTH=360599,CODECS="avc1.4D400D",RESOLUTION=416x234,URI="media-1/iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=121087,BANDWIDTH=631048,CODECS="avc1.4D400D",RESOLUTION=416x234,URI="media-2/iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=223837,BANDWIDTH=1171948,CODECS="avc1.4D401E",RESOLUTION=640x360,URI="media-3/iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=354946,BANDWIDTH=1752287,CODECS="avc1.4D401F",RESOLUTION=768x432,URI="media-4/iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=440896,BANDWIDTH=2343896,CODECS="avc1.4D401F",RESOLUTION=960x540,URI="media-5/iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=732176,BANDWIDTH=3887712,CODECS="avc1.4D401F",RESOLUTION=1280x720,URI="media-6/iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:AVERAGE-BANDWIDTH=1017054,BANDWIDTH=5747052,CODECS="avc1.640028",RESOLUTION=1920x1080,URI="media-7/iframes.m3u8"
```
* Parsed
```smalltalk
{
    "#EXTM3U": "",
    "#EXT-X-INDEPENDENT-SEGMENTS": "",
    "#EXT-X-VERSION": "7"
}
{
    "media": "threefive/media-4/stream.m3u8",
    "tags": {
        "#EXT-X-MEDIA": {
            "AUTOSELECT": "YES",
            "DEFAULT": "YES",
            "LANGUAGE": "en",
            "NAME": "CC1",
            "GROUP-ID": "text",
            "INSTREAM-ID": "CC1",
            "TYPE": "CLOSED-CAPTIONS"
        },
        "#EXT-X-STREAM-INF": {
            "CLOSED-CAPTIONS": "text",
            "RESOLUTION": "768x432",
            "CODECS": "avc1.4D401F,mp4a.40.2",
            "BANDWIDTH": "2127786",
            "AVERAGE-BANDWIDTH": "2030321"
        }
    }
}
{
    "media": "threefive/media-1/stream.m3u8",
    "tags": {
        "#EXT-X-STREAM-INF": {
            "CLOSED-CAPTIONS": "text",
            "RESOLUTION": "416x234",
            "CODECS": "avc1.4D400D,mp4a.40.2",
            "BANDWIDTH": "410181",
            "AVERAGE-BANDWIDTH": "393177"
        }
    }
}
{
    "media": "threefive/media-2/stream.m3u8",
    "tags": {
        "#EXT-X-STREAM-INF": {
            "CLOSED-CAPTIONS": "text",
            "RESOLUTION": "416x234",
            "CODECS": "avc1.4D400D,mp4a.40.2",
            "BANDWIDTH": "727459",
            "AVERAGE-BANDWIDTH": "698361"
        }
    }
}
{
    "media": "threefive/media-3/stream.m3u8",
    "tags": {
        "#EXT-X-STREAM-INF": {
            "CLOSED-CAPTIONS": "text",
            "RESOLUTION": "640x360",
            "CODECS": "avc1.4D401E,mp4a.40.2",
            "BANDWIDTH": "1263349",
            "AVERAGE-BANDWIDTH": "1210676"
        }
    }
}
{
    "media": "threefive/media-5/stream.m3u8",
    "tags": {
        "#EXT-X-STREAM-INF": {
            "CLOSED-CAPTIONS": "text",
            "RESOLUTION": "960x540",
            "CODECS": "avc1.4D401F,mp4a.40.2",
            "BANDWIDTH": "2913843",
            "AVERAGE-BANDWIDTH": "2748961"
        }
    }
}
{
    "media": "threefive/media-6/stream.m3u8",
    "tags": {
        "#EXT-X-STREAM-INF": {
            "CLOSED-CAPTIONS": "text",
            "RESOLUTION": "1280x720",
            "CODECS": "avc1.4D401F,mp4a.40.2",
            "BANDWIDTH": "5652395",
            "AVERAGE-BANDWIDTH": "5312128"
        }
    }
}
{
    "media": "threefive/media-7/stream.m3u8",
    "tags": {
        "#EXT-X-STREAM-INF": {
            "CLOSED-CAPTIONS": "text",
            "RESOLUTION": "1920x1080",
            "CODECS": "avc1.640028,mp4a.40.2",
            "BANDWIDTH": "8963399",
            "AVERAGE-BANDWIDTH": "8391745"
        }
    }
}
{
    "media": "threefive/media-1/iframes.m3u8",
    "tags": {
        "#EXT-X-I-FRAME-STREAM-INF": {
            "URI": "media-1/iframes.m3u8",
            "RESOLUTION": "416x234",
            "CODECS": "avc1.4D400D",
            "BANDWIDTH": "360599",
            "AVERAGE-BANDWIDTH": "64059"
        }
    }
}
{
    "media": "threefive/media-2/iframes.m3u8",
    "tags": {
        "#EXT-X-I-FRAME-STREAM-INF": {
            "URI": "media-2/iframes.m3u8",
            "RESOLUTION": "416x234",
            "CODECS": "avc1.4D400D",
            "BANDWIDTH": "631048",
            "AVERAGE-BANDWIDTH": "121087"
        }
    }
}
{
    "media": "threefive/media-3/iframes.m3u8",
    "tags": {
        "#EXT-X-I-FRAME-STREAM-INF": {
            "URI": "media-3/iframes.m3u8",
            "RESOLUTION": "640x360",
            "CODECS": "avc1.4D401E",
            "BANDWIDTH": "1171948",
            "AVERAGE-BANDWIDTH": "223837"
        }
    }
}
{
    "media": "threefive/media-4/iframes.m3u8",
    "tags": {
        "#EXT-X-I-FRAME-STREAM-INF": {
            "URI": "media-4/iframes.m3u8",
            "RESOLUTION": "768x432",
            "CODECS": "avc1.4D401F",
            "BANDWIDTH": "1752287",
            "AVERAGE-BANDWIDTH": "354946"
        }
    }
}
{
    "media": "threefive/media-5/iframes.m3u8",
    "tags": {
        "#EXT-X-I-FRAME-STREAM-INF": {
            "URI": "media-5/iframes.m3u8",
            "RESOLUTION": "960x540",
            "CODECS": "avc1.4D401F",
            "BANDWIDTH": "2343896",
            "AVERAGE-BANDWIDTH": "440896"
        }
    }
}
{
    "media": "threefive/media-6/iframes.m3u8",
    "tags": {
        "#EXT-X-I-FRAME-STREAM-INF": {
            "URI": "media-6/iframes.m3u8",
            "RESOLUTION": "1280x720",
            "CODECS": "avc1.4D401F",
            "BANDWIDTH": "3887712",
            "AVERAGE-BANDWIDTH": "732176"
        }
    }
}
{
    "media": "threefive/media-7/iframes.m3u8",
    "tags": {
        "#EXT-X-I-FRAME-STREAM-INF": {
            "URI": "media-7/iframes.m3u8",
            "RESOLUTION": "1920x1080",
            "CODECS": "avc1.640028",
            "BANDWIDTH": "5747052",
            "AVERAGE-BANDWIDTH": "1017054"
        }
    }
}
```
