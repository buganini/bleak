"""
retrieveConnectedPeripheralsWithServices
--------------

Example retrieving connected device with services uuid

Updated on 2023-05-04 by Buganini Chiu <buganini@b612.tw>

"""

import sys
sys.path.append("..")
import asyncio

from bleak import BleakScanner, BleakClient


async def main(services):
    def onDiscovered(peripheral, advertising_data):
        pass

    scanner = BleakScanner(onDiscovered)
    devices = scanner.retrieveConnectedPeripheralsWithServices(services)
    for d in devices:
        print(d)
        client = BleakClient(d, lambda *args: None)
        await client.connect()
        for service in client.services:
            print(service)
            for char in service.characteristics:
                print("  ", char)
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main([
        '00FF',
    ]))
