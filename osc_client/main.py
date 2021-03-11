import logging
import sys

import requests

stream_handler = logging.StreamHandler(sys.stdout)

logging.basicConfig(
    level=logging.INFO,
    format="[{%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
    handlers=[stream_handler],
)


class OSC:
    def __init__(
        self,
        protocol: str = "http",
        baseurl: str = "api.openstreetcam.org",
        version: str = "2.0",
    ):
        self.protocol = protocol
        self.baseurl = baseurl
        self.version = version
        self.requesturl = "{protocol}://{baseurl}/{version}/".format(
            protocol=self.protocol, baseurl=self.baseurl, version=self.version
        )

    def get_photos_from_point(
        self, lat: float, lng: float, zoomLevel: int = 12
    ) -> dict:
        """
        Gather filtered dictionary list from OSC photos request
        """
        logging.info(
            "Requesting OSC photos from lat,lng point: {}, {}".format(lat, lng)
        )

        # perform request
        result = requests.get(
            "{}photo".format(self.requesturl),
            params={"lat": lat, "lng": lng, "zoomLevel": zoomLevel},
        )

        if result.status_code == 200:

            # if we're successful in finding photos, return the results
            if result.json()["status"]["apiCode"] == 600:
                return result.json()["result"]["data"]

            # if the request is successful but we have no results, emit warning
            elif result.json()["status"]["apiCode"] == 601:
                raise Warning(
                    "Successful request but unable to find photos with those parameters."
                )
        else:

            # raise an error if something else went wrong with the request
            raise Exception("Unable to reach OSC or request may be malformed.")
