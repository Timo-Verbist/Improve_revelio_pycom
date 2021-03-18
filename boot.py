from network import WLAN
import machine
import pycom
import time
pycom.heartbeat(False)
wlan = WLAN(mode=WLAN.STA)

wlan.connect(ssid='telenet-9819F7E', auth=(WLAN.WPA2, 'x3cjkkmjrfhF'))
while not wlan.isconnected():
    machine.idle()
    print("wifi not connected")
    time.sleep(1)
    pycom.rgbled(0xFF0000)

print("WiFi connected succesfully")
print(wlan.ifconfig())
pycom.rgbled(0x00FF00)
