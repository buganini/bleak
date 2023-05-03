"""
retrieveConnectedPeripheralsWithServices
--------------

Example retrieving connected device with services uuid

Updated on 2023-05-04 by Buganini Chiu <buganini@b612.tw>

"""

import sys
sys.path.append("..")
import asyncio

from bleak import BleakScanner


async def main(services):
    def onDiscovered(peripheral, advertising_data):
        pass

    scanner = BleakScanner(onDiscovered)
    for d in scanner.retrieveConnectedPeripheralsWithServices(services):
        print(d)

if __name__ == "__main__":
    asyncio.run(main([
        '00FF',
    ]))
