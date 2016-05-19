# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-05-18 20:21:52
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-05-19 10:10:51
# @MIT License
# @http://tasdikrahman.me

"""
We want to visualize now how the above data would look at scale. Consider as
if right now we don't have data at scale ,so we come up with a plan to write
a script to simulate the use case where we have collected above data and a
lot other data from thousand's of devices .

Our visualization systems needs data ,so we need to build (fake )data at
our end (which includes id of the devices and mac ids ) to simulate the
use case. Consider a short case for now ,following should be the information
present at the end of building data set (for each device in dataset).

- Device id - ( N >= id > 0 )
- ethernet mac id
- wifi interface mac id

Task
====

Build a script which takes the input for number of
devices(N)(example- 100, 200, 1000) , generate data for N devices and
returns the generated data set containing data for these N number of devices.
"""

import sys
import random
import json

from exceptions import NegativeInput

class MACGen(object):

    def __init__(self, number):
        """
        initializes the number of devices for which thge MAC address is to
        be generated
        """
        if number < 0:
            raise NegativeInput("Number of devices cannot be negative")
        else:
            self.devices = number

    def _randomMAC(self):
        """
        Generates the random MAC addresses and returns any of the two randomly
        generated list of MAC address
        """

        mac_list = [
            [
                0x00, 0x16, 0x3e,
                random.randint(0x00, 0x7f),
                random.randint(0x00, 0xff),
                random.randint(0x00, 0xff)
            ],
            [
                0x01, 0x18, 0x3f,
                random.randint(0x01, 0x2f),
                random.randint(0x10, 0xfa),
                random.randint(0x10, 0xfc)
            ]
        ]
        return random.choice(mac_list)

    def _get_mac_address(self):
        """
        calls the _randomMAC() method and is in turn called by generate() to
        get the prettified MAC address
        """
        return ':'.join(map(lambda x: "%02x" % x, self._randomMAC()))

    def generate(self):
        """
        calls the method _randomMAC() and then appends the colon between
        the randomly selected bits and then saves it inside a flat dictionary
        """

        data_list = []
        for ID in range(self.devices):
            dict_data = {
                "device_id": ID,
                "wifi_mac_id": self._get_mac_address(),
                "ethernet_mac_id": self._get_mac_address()
            }
            data_list.append(dict_data)

        """writing this dictionary to a JSON file for easy access. This can be
        later written over to a csv file later on using appropriate tools"""

        device_data = {
            "device_data": data_list
        }

        with open('device_data.json', 'w') as f:
            f.write(json.dumps(
                        device_data,
                        indent=4,
                        sort_keys=True
                    )
            )

        print("Data generated for : {0} and written to 'device_data.json'".format(self.devices))


if __name__ == '__main__':
    # takes the argument (number of devices) passed from the command line

    """checking whether the user has passed any command line arguments or not
    and raising appropriate error message"""
    try:
        devices_num = int(sys.argv[1])
        MACObject = MACGen(devices_num)
        MACObject.generate()
    except IndexError as e:
        exception_msg = "You did not specify the number of devices for generating MAC addresses"
        raise Exception(exception_msg).with_traceback(e.__traceback__)
