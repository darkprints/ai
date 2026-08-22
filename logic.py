# logic.py
import supervisor
import storage
import board
import digitalio
import usb_cdc

# Leave this here if you want it configured early at startup
usb_cdc.enable(console=True, data=True)

def configure():
    # 1. Initialize your test pins safely
    j1 = digitalio.DigitalInOut(board.GP0)
    j1.switch_to_input(pull=digitalio.Pull.UP)
    j2 = digitalio.DigitalInOut(board.GP1)
    j2.switch_to_input(pull=digitalio.Pull.UP)

    # 2. Check the hardware conditions immediately at startup
    if not j1.value and not j2.value:
        print("Condition Met: USB Drive Enabled")
        storage.enable_usb_drive()
    else:
        print("Condition Failed: Disabling USB Drive (Stealth Mode)")
        storage.disable_usb_drive()

    # 3. Clean up the pins immediately so boot sequences exit cleanly
    j1.deinit()
    j2.deinit()

    # Register the file target safely
    supervisor.set_next_code_file(
        "peep.py",
        sticky_on_reload=True,
        sticky_on_success=True,
        sticky_on_error=True
    )
    
    # --- CRITICAL FIX: Completely removed supervisor.reload() from here! ---
