import os
import sys

sys.path.append(os.getcwd())

import pytest

from osc_client.main import OSC


osc = OSC()
sample_point = {"lat": 34.94083565649461, "lng": -82.8662492514243}


def test_init():

    found_attributes = [attribute for attribute in dir(osc) if "__" not in attribute]
    expected_attributes = [
        "baseurl",
        "get_photos_from_point",
        "protocol",
        "requesturl",
        "version",
    ]
    assert found_attributes == expected_attributes


def test_get_photos_from_point():

    expected_keys = [
        "autoImgProcessingResult",
        "autoImgProcessingStatus",
        "cameraParameters",
        "dateAdded",
        "dateProcessed",
        "distance",
        "fieldOfView",
        "filepath",
        "filepathLTh",
        "filepathProc",
        "filepathTh",
        "fileurl",
        "fileurlLTh",
        "fileurlProc",
        "fileurlTh",
        "from",
        "gpsAccuracy",
        "hasObd",
        "heading",
        "height",
        "id",
        "imagePartProjection",
        "isUnwrapped",
        "isWrapped",
        "lat",
        "lng",
        "matchLat",
        "matchLng",
        "matchSegmentId",
        "name",
        "projection",
        "projectionYaw",
        "qualityDetails",
        "qualityLevel",
        "qualityStatus",
        "rawDataId",
        "sequenceId",
        "sequenceIndex",
        "shotDate",
        "status",
        "storage",
        "to",
        "unwrapVersion",
        "videoId",
        "videoIndex",
        "visibility",
        "wayId",
        "width",
        "wrapVersion",
    ]
    result = osc.get_photos_from_point(lat=sample_point["lat"], lng=sample_point["lng"])

    assert len(expected_keys) == len(list(result[0].keys()))
