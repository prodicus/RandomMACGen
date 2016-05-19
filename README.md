## Random MAC Address Generator

So simply put, we have to generate MAC addresses for the

- WI-FI interface
- ethernet interface

for the number of devices passed as the command line argument

## Installation

**Clone it**

`$ git clone https://github.com/prodicus/RandomMACGen && cd RandomMACGen/RandomMACGen`

## Running it

`$ python3 MAC_generator.py <NUMBER_OF_DEVICES>`

## Sample run

`$ python3 MAC_generator.py 30`

A sample run for 30 devices has been stores inside the file ['device_data.json'](https://github.com/prodicus/RandomMACGen/blob/master/RandomMACGen/device_data.json)

The `json` file was validated using [`json-spec`](https://pypi.python.org/pypi/json-spec) module by doing a

`$ json validate --schema-file=schema.json < device_data.json`

**or**

you can simply go to [http://jsonlint.com/](http://jsonlint.com/) for validating the `JSON`

## Extracting data from the `JSON` file

So supposedly you have the wish to extract the MAC ID's for devices with device ID's `[20, 8, 23, 12]`

```python
>>> import os
>>> import json
>>>
>>> filename = 'device_data.json'
>>> os.path.isfile(filename)  # checking for file existance
True
>>> file_content = open(filename, 'r').read()
>>> json_data = json.loads(file_content)
>>> type(json_data)
<class 'dict'>
>>>
>>> device_list = [20, 8, 23, 12]
>>>
>>> for device in device_list:
...   print("device_id => {0} : wifi-mac => {1} : ethernet-mac => {2}".format(
...             device,
...             json_data["device_data"][device]["wifi_mac_id"],
...             json_data["device_data"][device]["ethernet_mac_id"]
...         )
...   )
...
device_id => 20 : wifi-mac => 01:18:3f:1d:ea:32 : ethernet-mac => 00:16:3e:08:1a:fb
device_id => 8 : wifi-mac => 01:18:3f:2b:5c:f2 : ethernet-mac => 01:18:3f:14:21:97
device_id => 23 : wifi-mac => 00:16:3e:41:d4:b7 : ethernet-mac => 01:18:3f:1f:6a:c9
device_id => 12 : wifi-mac => 00:16:3e:13:f4:bc : ethernet-mac => 00:16:3e:59:f7:e8
>>>
```

## License

MIT Licensed © 2016 by [Tasdik Rahman](http://tasdikrahman.me)

You can find a copy of the License at the [license file](https://github.com/prodicus/RandomMACGen/blob/master/LICENSE)