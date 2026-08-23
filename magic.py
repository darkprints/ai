import supervisor
import board
import digitalio
import time
import neopixel

strip1 = neopixel.NeoPixel(board.GP15, 15)
strip2 = neopixel.NeoPixel(board.GP16, 15)

red = (255, 0, 0)
green = (0, 255, 0)

j1 = digitalio.DigitalInOut(board.GP0)
j1.switch_to_input(pull=digitalio.Pull.UP)
j2 = digitalio.DigitalInOut(board.GP1)
j2.switch_to_input(pull=digitalio.Pull.UP)

if not j1.value and not j2.value:
    strip1.fill(red)
    strip2.fill(green)
    time.sleep(10)

    j1.deinit()
    j2.deinit()

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

    j1.deinit()
    j2.deinit()

    supervisor.set_next_code_file(
        "findme.py",
        reload_on_success=True,
        reload_on_error=True,
        sticky_on_reload=True,
        sticky_on_success=True,
        sticky_on_error=True
    )
    supervisor.reload()
