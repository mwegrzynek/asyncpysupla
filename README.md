AsyncPySupla
============

A simplistic (and incomplete!) async wrapper for [Supla's OpenAPI](https://cloud.supla.org/api/docs.html), used mainly for [HomeAssistant](https://www.home-assistant.io/) integration.

This is [PySupla's](https://github.com/mwegrzynek/pysupla) sister library.

I'm in no way affiliated with Supla and Zamel: I love their devices, but prefer to use all my Smart Home devices from one app.

See tests directory for usage examples.

Currently, there are only integration tests: to run them, you have to export the following environmental variables:

* SUPLA_SERVER - an address of Supla's cloud server you want to test against (ex. srv1.supla.org, or (better) your own test instance).

* SUPLA_PERSONAL_ACCESS_TOKEN - a personal access token you can get [here](https://cloud.supla.org/integrations/tokens) (if you use Supla's server of course). PySupla currently does not support OAuth2.

* SUPLA_SHUTTER_ID - an ID of a shutter type device to test against (this is what I'm mainly using Supla for).

Contributors welcome!