# OCP Bandcamp Plugin

This plugin lets OVOS Common Play (OCP) play Bandcamp URLs. It extracts the real stream URL at playback time.

## Install

```bash
pip install ovos-ocp-bandcamp-plugin
```

## Usage

OCP loads this plugin through the `opm.ocp.extractor` entry point. No manual setup is needed.

The plugin handles a URL in two cases:
- The URL contains `bandcamp.`.
- The URL uses the `bandcamp//` stream extractor ID (sei) prefix, for example `bandcamp//https://artist.bandcamp.com/track/some-song`.

When OCP asks the plugin to extract a stream, the plugin calls [py_bandcamp](https://github.com/TigreGotico/py_bandcamp) to fetch the playable stream data.

## Related projects

- [TigreGotico/py_bandcamp](https://github.com/TigreGotico/py_bandcamp): the Bandcamp scraper this plugin uses to extract streams.
- [OpenVoiceOS/ovos-plugin-manager](https://github.com/OpenVoiceOS/ovos-plugin-manager): defines the `OCPStreamExtractor` template this plugin implements.
- [OpenVoiceOS/ovos-ocp-youtube-plugin](https://github.com/OpenVoiceOS/ovos-ocp-youtube-plugin): a sibling OCP stream extractor plugin for YouTube.

## License

Apache-2.0
