import supervisor
import storage
import board
import digitalio
import usb_cdc
import fun

usb_cdc.enable(console=True, data=True)

def lumination_logic():

    fun.config()


    j1 = digitalio.DigitalInOut(board.GP0)
    j1.switch_to_input(pull=digitalio.Pull.UP)
    j2 = digitalio.DigitalInOut(board.GP1)
    j2.switch_to_input(pull=digitalio.Pull.UP)

    if not j1.value and not j2.value:
        storage.enable_usb_drive()
    else:
        storage.disable_usb_drive()

    j1.deinit()
    j2.deinit()

    supervisor.set_next_code_file(
        "magic.py",
        sticky_on_reload=True,
        sticky_on_success=True,
        sticky_on_error=True
    )