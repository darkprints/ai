import supervisor
import board
import digitalio
import time
import neopixel
import usb_cdc

usb_cdc.enable(console=True, data=True)

strip1 = neopixel.NeoPixel(board.GP15, 15)
strip2 = neopixel.NeoPixel(board.GP16, 15)

red = (255, 0, 0)
green = (0, 255, 0)



# 1. Re-initialize the test pins inside the running logic space
j1 = digitalio.DigitalInOut(board.GP0)
j1.switch_to_input(pull=digitalio.Pull.UP)
j2 = digitalio.DigitalInOut(board.GP1)
j2.switch_to_input(pull=digitalio.Pull.UP)

# 2. Execute your targeted routing logic
if not j1.value and not j2.value:
    # Run your animations and delay safely here in code.py
    strip1.fill(red)
    strip2.fill(green)
    time.sleep(10)
    
    # Clean up the hardware variables BEFORE resetting
    j1.deinit()
    j2.deinit()
    
    # Configure path to main2.py securely using 9.x rules
    supervisor.set_next_code_file(
        "two.py", 
        sticky_on_reload=True, 
        sticky_on_success=True, 
        sticky_on_error=True
    )
    supervisor.reload()

else:
    # Clean up the hardware variables BEFORE resetting
    j1.deinit()
    j2.deinit()
    
    # Configure path to main.py securely using 9.x rules
    supervisor.set_next_code_file(
        "step.py", 
        sticky_on_reload=True, 
        sticky_on_success=True, 
        sticky_on_error=True
    )
    supervisor.reload()
