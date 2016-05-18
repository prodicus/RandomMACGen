## Random MAC Address Generator

So simply put, we have to generate MAC addresses for the

- WI-FI interface
- ethernet interface

for the number of devices passed as the command line argument

## Installation

**Clone it**

`$ git clone https://github.com/prodicus/RandomMACGen && cd RandomMACGen`

## Running it

`$ python3 MAC_generator.py <NUMBER_OF_DEVICES>`

## Sample run

`$ python3 MAC_generator.py 30`

A sample run for 30 devices has been stores inside the file ['device_data.json'](https://github.com/prodicus/RandomMACGen/blob/master/device_data.json)

The `json` file was validated using [`json-spec`](https://pypi.python.org/pypi/json-spec) module by doing a 

`$ json validate --schema-file=schema.json < device_data.json`

**or**

you can simply go to [http://jsonlint.com/](http://jsonlint.com/) for validating the `JSON`

## License

MIT Licensed © 2016 by [Tasdik Rahman](http://tasdikrahman.me)

You can find a copy of the License at the [license file](https://github.com/prodicus/RandomMACGen/blob/master/LICENSE)