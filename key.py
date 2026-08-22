import microcontroller
import usb_cdc
import storage
import supervisor
import board
import digitalio
import time
import neopixel

def job_sys():
    usb_cdc.enable(console=True, data=True)

job_bytes = b"fun" + b" " * 10 

microcontroller.nvm[0:len(job_bytes)] = job_bytes
