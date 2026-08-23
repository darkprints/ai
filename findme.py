import microcontroller
import __main__
import sys

raw_bytes = microcontroller.nvm[0:13]

target_mpy_name = raw_bytes.decode("utf-8").strip(" \x00")

if target_mpy_name and target_mpy_name != "":
    
    try:
        __import__(target_mpy_name)
        
    except ImportError as e:
        print(f"Error: Could not execute /lib/{target_mpy_name}.mpy. Details: {e}")
else:
    print("Error")