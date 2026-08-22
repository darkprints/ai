import microcontroller
import sys

print("--- Phase 2: Main Execution ---")

# 1. Read the raw binary bytes straight out of the hardware register space
raw_bytes = microcontroller.nvm[0:13]

# 2. Convert the bytes back into clean text and strip out the blank spacers
target_mpy_name = raw_bytes.decode("utf-8").strip()

if target_mpy_name and target_mpy_name != "":
    print(f"Hardware NVM variable found! Target: {target_mpy_name}.mpy")
    
    try:
        # Clear out old caches if they exist
        if target_mpy_name in sys.modules:
            del sys.modules[target_mpy_name]
            
        # 3. Natively load and execute the file from your /lib folder layout
        __import__(target_mpy_name)
        print("Success! The .mpy file is running.")
        
    except ImportError as e:
        print(f"Error: Could not find {target_mpy_name}.mpy inside /lib. Details: {e}")
else:
    print("Error: The chip hardware NVM registers were empty.")