from ovos_plugin_manager.templates.ocp import OCPStreamExtractor
from py_bandcamp.utils import get_stream_data


class OCPBandcampExtractor(OCPStreamExtractor):

    def __init__(self, ocp_settings=None):
        super().__init__(ocp_settings)
        self.settings = self.ocp_settings.get("bandcamp", {})

    @property
    def supported_seis(self):
        """
        skills may return results requesting a specific extractor to be used

        plugins should report a StreamExtractorIds (sei) that identifies it can handle certain kinds of requests

        any streams of the format "{sei}//{uri}" can be handled by this plugin
        """
        return ["bandcamp"]

    def validate_uri(self, uri):
        """ return True if uri can be handled by this extractor, False otherwise"""
        return any([uri.startswith(sei) for sei in self.supported_seis]) or \
               self.is_bandcamp(uri)

    def extract_stream(self, url, video=True):
        """ return the real uri that can be played by OCP """
        data = get_stream_data(url)
        data["uri"] = data.pop("stream")
        return data

    @staticmethod
    def is_bandcamp(url):
        if not url:
            return False
        return "bandcamp." in url


