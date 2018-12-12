#!/usr/bin/env python3.6

from sys import argv
from meross_iot.api import MerossHttpClient

mDev = int(argv[1])
mCh  = argv[2]          # ch 1-2-3-USB
mVal = int(argv[3])     # 0 = Off / 1 = On

print("parametri:" + argv[1] + " / " + argv[2] + " / " + argv[3])

mConnect = MerossHttpClient(email="YOUR REGISTERED EMAIL", password="YOUR PASSWORD")
mDevices = mConnect.list_supported_devices()

if mCh != "USB":
        mCh = int(mCh)
        if mVal == 0:
                mDevices[mDev].turn_off_channel(mCh)
        else:
                mDevices[mDev].turn_on_channel(mCh)
else:
        if int(mVal) == 0:
                print("DISABILITA USB")
                mDevices[mDev].disable_usb()
        else:
                print("ABILITA USB")
                mDevices[mDev].enable_usb()
