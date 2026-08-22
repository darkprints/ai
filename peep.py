# peep.py
import supervisor
import board
import digitalio
import time
import neopixel

print("--- [peep.py] Environment Loaded Successfully ---")

# Setup your strips cleanly
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
    print("Match Found! Illuminating and transitioning to two.py")
    strip1.fill(red)
    strip2.fill(green)
    time.sleep(10)

    # Clean up the hardware variables BEFORE resetting
    j1.deinit()
    j2.deinit()

    # Use all execution flags to force transition to two.py
    supervisor.set_next_code_file(
        "two.py",
        reload_on_success=True,
        reload_on_error=True,
        sticky_on_reload=True,
        sticky_on_success=True,
        sticky_on_error=True
    )
    supervisor.reload()

else:
    print("No Match! Cleaning up and moving to step.py")
    
    # Clean up the hardware variables BEFORE resetting
    j1.deinit()
    j2.deinit()

    # Use all execution flags to force transition to step.py
    supervisor.set_next_code_file(
        "launch_three.py",
        reload_on_success=True,
        reload_on_error=True,
        sticky_on_reload=True,
        sticky_on_success=True,
        sticky_on_error=True
    )
    supervisor.reload()
