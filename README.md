# hls
M3U8 Parser with full SCTE-35 Support

* All HLS Tags are Supported.
* Private / Custom Tags are Supported.
* HTTP(S), Multicast,UDP, and File URIs are Supported
* Base64, Bytes, and Hex formated SCTE-35 Cues are Supported.
*   


### Usage:
```
a@fumatica:~/m3u8fu$ pypy3  m3u8fu.py ../threefive/scte35.m3u8
```
### Returns JSON 
```smalltalk
{
    "headers": {
        "#EXTM3U": "",
        "#EXT-X-VERSION": "3",
        "#EXT-X-TARGETDURATION": "12",
        "#EXT-X-MEDIA-SEQUENCE": "1",
        "#EXT-X-PLAYLIST-TYPE": "VOD"
    },
    "media": [
        {
            "media": "file_60p_1_00001.ts",
            "end": 10.0,
            "duration": 10.0,
            "tags": {
                "#EXTINF": 10.0
            }
        },
```
* __SCTE-35 Cues are parsed and the data is included__
```
        {
            "media": "seg70.ts",
            "start": 147.157,
            "end": 148.058,
            "duration": 0.901,
            "cue": "/DAlAAAAAAAAAAAAFAUAAABXf+//iNg15n4Ae97wAAECAQAAtBIorQ==",
            "cue_data": {
                "info_section": {
                    "table_id": "0xfc",
                    "section_syntax_indicator": false,
                    "private": false,
                    "sap_type": "0x3",
                    "sap_details": "No Sap Type",
                    "section_length": 37,
                    "protocol_version": 0,
                    "encrypted_packet": false,
                    "encryption_algorithm": 0,
                    "pts_adjustment_ticks": 0,
                    "pts_adjustment": 0.0,
                    "cw_index": "0x0",
                    "tier": "0x0",
                    "splice_command_length": 20,
                    "splice_command_type": 5,
                    "descriptor_loop_length": 0,
                    "crc": "0xb41228ad"
                },
                "command": {
                    "command_length": 20,
                    "command_type": 5,
                    "name": "Splice Insert",
                    "time_specified_flag": true,
                    "pts_time": 73231.536067,
                    "pts_time_ticks": 6590838246,
                    "break_auto_return": false,
                    "break_duration": 90.2,
                    "break_duration_ticks": 8118000,
                    "splice_event_id": 87,
                    "splice_event_cancel_indicator": false,
                    "out_of_network_indicator": true,
                    "program_splice_flag": true,
                    "duration_flag": true,
                    "splice_immediate_flag": false,
                    "unique_program_id": 1,
                    "avail_num": 2,
                    "avail_expected": 1
                },
                "descriptors": []
            },
            "tags": {
                "#EXT-X-SCTE35": {
                    "CUE-OUT": "YES",
                    "CUE": "/DAlAAAAAAAAAAAAFAUAAABXf+//iNg15n4Ae97wAAECAQAAtBIorQ=="
                },
                "#EXTINF": 0.901
            }
        },

```
        {
            "media": "file_60p_1_00003.ts",
            "start": 12.0,
            "end": 24.0,
            "duration": 12.0,
            "cue": "/DAnAAAAAAAAAP/wBQb+AA27oAARAg9DVUVJAAAAAX+HCQA0AAE0xUZn",
            "tags": {
                "#EXT-X-CUE-OUT-CONT": {
                    "SCTE35": "/DAnAAAAAAAAAP/wBQb+AA27oAARAg9DVUVJAAAAAX+HCQA0AAE0xUZn",
                    "Duration": 30,
                    "ElapsedTime": 2.0
                },
                "#EXTINF": 12.0
            }
        },
        {
            "media": "file_60p_1_00004.ts",
            "start": 24.0,
            "end": 36.0,
            "duration": 12.0,
            "cue": "/DAnAAAAAAAAAP/wBQb+AA27oAARAg9DVUVJAAAAAX+HCQA0AAE0xUZn",
            "tags": {
                "#EXT-X-CUE-OUT-CONT": {
                    "SCTE35": "/DAnAAAAAAAAAP/wBQb+AA27oAARAg9DVUVJAAAAAX+HCQA0AAE0xUZn",
                    "Duration": 30,
                    "ElapsedTime": 14.0
                },
                "#EXTINF": 12.0
            }
        },
  ...
  
  ```

###        {
            "media": "seg70.ts",
            "start": 147.157,
            "end": 148.058,
            "duration": 0.901,
            "cue": "/DAlAAAAAAAAAAAAFAUAAABXf+//iNg15n4Ae97wAAECAQAAtBIorQ==",
            "cue_data": {
                "info_section": {
                    "table_id": "0xfc",
                    "section_syntax_indicator": false,
                    "private": false,
                    "sap_type": "0x3",
                    "sap_details": "No Sap Type",
                    "section_length": 37,
                    "protocol_version": 0,
                    "encrypted_packet": false,
                    "encryption_algorithm": 0,
                    "pts_adjustment_ticks": 0,
                    "pts_adjustment": 0.0,
                    "cw_index": "0x0",
                    "tier": "0x0",
                    "splice_command_length": 20,
                    "splice_command_type": 5,
                    "descriptor_loop_length": 0,
                    "crc": "0xb41228ad"
                },
                "command": {
                    "command_length": 20,
                    "command_type": 5,
                    "name": "Splice Insert",
                    "time_specified_flag": true,
                    "pts_time": 73231.536067,
                    "pts_time_ticks": 6590838246,
                    "break_auto_return": false,
                    "break_duration": 90.2,
                    "break_duration_ticks": 8118000,
                    "splice_event_id": 87,
                    "splice_event_cancel_indicator": false,
                    "out_of_network_indicator": true,
                    "program_splice_flag": true,
                    "duration_flag": true,
                    "splice_immediate_flag": false,
                    "unique_program_id": 1,
                    "avail_num": 2,
                    "avail_expected": 1
                },
                "descriptors": []
            },
            "tags": {
                "#EXT-X-SCTE35": {
                    "CUE-OUT": "YES",
                    "CUE": "/DAlAAAAAAAAAAAAFAUAAABXf+//iNg15n4Ae97wAAECAQAAtBIorQ=="
                },
                "#EXTINF": 0.901
            }
        }
 ```
 
   *  __Master Playlists are also Supported__

```smalltalk
a@fumatica:~/m3u8fu$ pypy3  m3u8fu.py ../threefive/master.m3u8 
{
    "headers": {
        "#EXTM3U": "",
        "#EXT-X-INDEPENDENT-SEGMENTS": "",
        "#EXT-X-VERSION": "7"
    },
    "media": [
        {
            "media": "media-4/stream.m3u8",
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
                    "BANDWIDTH": 2127786,
                    "AVERAGE-BANDWIDTH": 2030321
                }
            }
        },
        {
            "media": "media-1/stream.m3u8",
            "tags": {
                "#EXT-X-STREAM-INF": {
                    "CLOSED-CAPTIONS": "text",
                    "RESOLUTION": "416x234",
                    "CODECS": "avc1.4D400D,mp4a.40.2",
                    "BANDWIDTH": 410181,
                    "AVERAGE-BANDWIDTH": 393177
                }
            }
        },
        {
            "media": "media-2/stream.m3u8",
            "tags": {
                "#EXT-X-STREAM-INF": {
                    "CLOSED-CAPTIONS": "text",
                    "RESOLUTION": "416x234",
                    "CODECS": "avc1.4D400D,mp4a.40.2",
                    "BANDWIDTH": 727459,
                    "AVERAGE-BANDWIDTH": 698361
                }
            }
        },
        {
            "media": "media-3/stream.m3u8",
            "tags": {
                "#EXT-X-STREAM-INF": {
                    "CLOSED-CAPTIONS": "text",
                    "RESOLUTION": "640x360",
                    "CODECS": "avc1.4D401E,mp4a.40.2",
                    "BANDWIDTH": 1263349,
                    "AVERAGE-BANDWIDTH": 1210676
                }
            }
        },
        {
            "media": "media-5/stream.m3u8",
            "tags": {
                "#EXT-X-STREAM-INF": {
                    "CLOSED-CAPTIONS": "text",
                    "RESOLUTION": "960x540",
                    "CODECS": "avc1.4D401F,mp4a.40.2",
                    "BANDWIDTH": 2913843,
                    "AVERAGE-BANDWIDTH": 2748961
                }
            }
        },
        {
            "media": "media-6/stream.m3u8",
            "tags": {
                "#EXT-X-STREAM-INF": {
                    "CLOSED-CAPTIONS": "text",
                    "RESOLUTION": "1280x720",
                    "CODECS": "avc1.4D401F,mp4a.40.2",
                    "BANDWIDTH": 5652395,
                    "AVERAGE-BANDWIDTH": 5312128
                }
            }
        },
        {
            "media": "media-7/stream.m3u8",
            "tags": {
                "#EXT-X-STREAM-INF": {
                    "CLOSED-CAPTIONS": "text",
                    "RESOLUTION": "1920x1080",
                    "CODECS": "avc1.640028,mp4a.40.2",
                    "BANDWIDTH": 8963399,
                    "AVERAGE-BANDWIDTH": 8391745
                }
            }
        },
        {
            "media": "media-1/iframes.m3u8",
            "tags": {
                "#EXT-X-I-FRAME-STREAM-INF": {
                    "URI": "media-1/iframes.m3u8",
                    "RESOLUTION": "416x234",
                    "CODECS": "avc1.4D400D",
                    "BANDWIDTH": 360599,
                    "AVERAGE-BANDWIDTH": 64059
                }
            }
        },
        {
            "media": "media-2/iframes.m3u8",
            "tags": {
                "#EXT-X-I-FRAME-STREAM-INF": {
                    "URI": "media-2/iframes.m3u8",
                    "RESOLUTION": "416x234",
                    "CODECS": "avc1.4D400D",
                    "BANDWIDTH": 631048,
                    "AVERAGE-BANDWIDTH": 121087
                }
            }
        },
        {
            "media": "media-3/iframes.m3u8",
            "tags": {
                "#EXT-X-I-FRAME-STREAM-INF": {
                    "URI": "media-3/iframes.m3u8",
                    "RESOLUTION": "640x360",
                    "CODECS": "avc1.4D401E",
                    "BANDWIDTH": 1171948,
                    "AVERAGE-BANDWIDTH": 223837
                }
            }
        },
        {
            "media": "media-4/iframes.m3u8",
            "tags": {
                "#EXT-X-I-FRAME-STREAM-INF": {
                    "URI": "media-4/iframes.m3u8",
                    "RESOLUTION": "768x432",
                    "CODECS": "avc1.4D401F",
                    "BANDWIDTH": 1752287,
                    "AVERAGE-BANDWIDTH": 354946
                }
            }
        },
        {
            "media": "media-5/iframes.m3u8",
            "tags": {
                "#EXT-X-I-FRAME-STREAM-INF": {
                    "URI": "media-5/iframes.m3u8",
                    "RESOLUTION": "960x540",
                    "CODECS": "avc1.4D401F",
                    "BANDWIDTH": 2343896,
                    "AVERAGE-BANDWIDTH": 440896
                }
            }
        },
        {
            "media": "media-6/iframes.m3u8",
            "tags": {
                "#EXT-X-I-FRAME-STREAM-INF": {
                    "URI": "media-6/iframes.m3u8",
                    "RESOLUTION": "1280x720",
                    "CODECS": "avc1.4D401F",
                    "BANDWIDTH": 3887712,
                    "AVERAGE-BANDWIDTH": 732176
                }
            }
        },
        {
            "media": "media-7/iframes.m3u8",
            "tags": {
                "#EXT-X-I-FRAME-STREAM-INF": {
                    "URI": "media-7/iframes.m3u8",
                    "RESOLUTION": "1920x1080",
                    "CODECS": "avc1.640028",
                    "BANDWIDTH": 5747052,
                    "AVERAGE-BANDWIDTH": 1017054
                }
            }
        }
    ]
}
```
