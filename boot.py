from network import WLAN
import machine
import pycom
import time
pycom.heartbeat(False)
wlan = WLAN(mode=WLAN.STA)

wlan.connect(ssid='IoT', auth=(WLAN.WPA2, 'KdGIoT92!'))
while not wlan.isconnected():
    machine.idle()
    print("wifi not connected")
    time.sleep(1)
    pycom.rgbled(0xFF0000)

print("WiFi connected succesfully")
print(wlan.ifconfig())
pycom.rgbled(0x00FF00)
