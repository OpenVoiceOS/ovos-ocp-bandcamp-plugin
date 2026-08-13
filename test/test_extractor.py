import unittest
from unittest.mock import patch

from ovos_ocp_bandcamp_plugin import (
    OCPBandcampExtractor,
    OCPBandcampExtractorConfig,
)


class TestOCPBandcampExtractor(unittest.TestCase):

    def setUp(self):
        self.extractor = OCPBandcampExtractor()

    def test_supported_seis(self):
        self.assertEqual(OCPBandcampExtractor.supported_seis, ["bandcamp"])

    def test_is_bandcamp(self):
        self.assertTrue(
            OCPBandcampExtractor.is_bandcamp("https://artist.bandcamp.com/track/x")
        )
        self.assertTrue(
            OCPBandcampExtractor.is_bandcamp("http://bandcamp.com/foo")
        )
        self.assertFalse(
            OCPBandcampExtractor.is_bandcamp("https://youtube.com/watch?v=x")
        )
        self.assertFalse(OCPBandcampExtractor.is_bandcamp(""))
        self.assertFalse(OCPBandcampExtractor.is_bandcamp(None))

    def test_validate_uri(self):
        # matches via sei prefix
        self.assertTrue(self.extractor.validate_uri("bandcamp//some-id"))
        # matches via is_bandcamp host check
        self.assertTrue(
            self.extractor.validate_uri("https://artist.bandcamp.com/album/x")
        )
        # unrelated uri
        self.assertFalse(
            self.extractor.validate_uri("https://youtube.com/watch?v=x")
        )

    def test_settings_from_ocp(self):
        ext = OCPBandcampExtractor({"bandcamp": {"foo": "bar"}})
        self.assertEqual(ext.settings, {"foo": "bar"})

    def test_settings_default(self):
        self.assertEqual(self.extractor.settings, {})

    def test_extract_stream_strips_sei_prefix(self):
        """regression for https://github.com/OpenVoiceOS/ovos-ocp-bandcamp-plugin/issues/2

        "bandcamp//<url>" (the sei-prefixed uri OCP hands extractors) must
        have the "bandcamp//" prefix stripped before being handed to
        py_bandcamp, otherwise requests blows up with
        `InvalidSchema: No connection adapters were found for 'bandcamp//https://...'`
        """
        real_url = "https://dr1p.bandcamp.com/track/flowerbomb"
        with patch("ovos_ocp_bandcamp_plugin.get_stream_data") as mocked:
            mocked.return_value = {"stream": "https://example.com/stream.mp3"}
            self.extractor.extract_stream(f"bandcamp//{real_url}")
        mocked.assert_called_once_with(real_url)


class TestOCPBandcampExtractorConfig(unittest.TestCase):

    def test_config_shape(self):
        self.assertIsInstance(OCPBandcampExtractorConfig, dict)
        self.assertIn("bandcamp", OCPBandcampExtractorConfig)


if __name__ == "__main__":
    unittest.main()
