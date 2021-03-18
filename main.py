from machine import UART
import time

uart = UART(1, 9600)
uart.init(baudrate=9600, bits=8, parity=None, stop=1, timeout_chars=100)
# the standard pins are p3 and p4, so you don't need to name them

while True:
    header_bytes = uart.read(1)
    while(header_bytes != b'\xff'):
        header_bytes=uart.read(1)

    data_high = int(uart.read(1)[0])
    data_low = int(uart.read(1)[0])
    data_sum = int(uart.read(1)[0])
    sum = data_high + data_low
    if (sum == data_sum + 1):
        distance = (data_high*256 + data_low)
        calc = "{:6.2f}".format(distance)
        # total length of 6 and after the comma max 2 digits.
        # (eg. 6.2f  386.231  ->  386.23)
        print("The distance is " + str(calc) + " mm")
        # data_high is 0, 1 or 2
        # data_low is a number between 0 and 255.
        # if data_low goes past 255, it starts again from 0
        # and data_high rises with 1
        # time.sleep(0.2)
