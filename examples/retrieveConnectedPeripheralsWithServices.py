"""
Scan/Discovery
--------------

Example showing how to scan for BLE devices.

Updated on 2019-03-25 by hbldh <henrik.blidh@nedomkull.com>

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
