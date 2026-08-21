import time
import board
import digitalio
import neopixel
import storage
import usb_cdc

from my_animations import *

button = digitalio.DigitalInOut(board.GP0)
button.switch_to_input(pull=digitalio.Pull.UP)

horn = digitalio.DigitalInOut(board.GP1)
horn.switch_to_input(pull=digitalio.Pull.UP)

strip1 = neopixel.NeoPixel(board.GP15, 15, brightness=0.1)
strip2 = neopixel.NeoPixel(board.GP16, 15, brightness=0.1)
strip3 = neopixel.NeoPixel(board.GP14, 8,)
strip4 = neopixel.NeoPixel(board.GP13, 14,)
strip5 = neopixel.NeoPixel(board.GP18, 14,)
strip6 = neopixel.NeoPixel(board.GP6, 15,)
strip7 = neopixel.NeoPixel(board.GP27, 15,)
strip8 = neopixel.NeoPixel(board.GP28, 11,)
strip9 = neopixel.NeoPixel(board.GP5, 11,)

red = (255, 0, 0)
orange = (255, 165, 0)
magenta = (255, 51, 255)
yellow = (255, 150, 0)
green = (0, 255, 0)
ltgreen = (51, 255, 51)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
white = (255, 255, 255)
colors_rgb = (red, orange, yellow, green, blue, indigo, violet)
cyan = (0, 255, 255)
lightblue = (153, 204, 255)
pink = (255, 153, 204)
black = (0, 0, 0)

sequence = AnimationSequence(
    AnimationGroup(
        Solid(strip1, color=cyan),
        Solid(strip2, color=cyan),
    ),
    AnimationGroup(
        Solid(strip1, color=red),
        Solid(strip2, color=red),
    ),
    AnimationGroup(
        Chase(strip1, speed=0.03, size=3, spacing=12, color=cyan),
        Chase(strip2, speed=0.03, size=3, spacing=12, color=cyan),
    ),
    AnimationGroup(
        Solid(strip1, color=black),
        Solid(strip2, color=black),
    ),
)

sequence2 = AnimationSequence(
    AnimationGroup(
        Solid(strip3, color=magenta),
        Solid(strip4, color=magenta),
        Solid(strip5, color=magenta),
        Solid(strip6, color=magenta),
        Solid(strip7, color=magenta),
        Solid(strip8, color=magenta),
        Solid(strip9, color=magenta),        
    ),
    AnimationGroup(
        Blink(strip3, speed=0.2, color=cyan),
        Blink(strip4, speed=0.2, color=cyan),
        Blink(strip5, speed=0.2, color=cyan),
        Blink(strip6, speed=0.2, color=cyan),
        Blink(strip7, speed=0.2, color=cyan),
        Blink(strip8, speed=0.2, color=cyan),
        Blink(strip9, speed=0.2, color=cyan),
    ),
    AnimationGroup(
        Chase(strip3, speed=.05, size=3, spacing=12, color=cyan),
        Chase(strip4, speed=.05, size=3, spacing=12, color=cyan),
        Chase(strip5, speed=.05, size=3, spacing=12, color=cyan),
        Chase(strip6, speed=.05, size=3, spacing=12, color=cyan),
        Chase(strip7, speed=.05, size=3, spacing=12, color=cyan),
        Chase(strip8, speed=.05, size=3, spacing=12, color=cyan),
        Chase(strip9, speed=.05, size=3, spacing=12, color=cyan),
    ),
    AnimationGroup(
        CustomColorChase(strip3, speed=.05, size=3, spacing=2, reverse=False, colors=[red, orange, blue]),
        CustomColorChase(strip4, speed=.05, size=3, spacing=2, reverse=False, colors=[red, orange, blue]),
        CustomColorChase(strip5, speed=.05, size=3, spacing=2, reverse=False, colors=[red, orange, blue]),
        CustomColorChase(strip6, speed=.05, size=3, spacing=2, reverse=False, colors=[red, orange, blue]),
        CustomColorChase(strip7, speed=.05, size=3, spacing=2, reverse=False, colors=[red, orange, blue]),
        CustomColorChase(strip8, speed=.05, size=3, spacing=2, reverse=False, colors=[red, orange, blue]),
        CustomColorChase(strip9, speed=.05, size=3, spacing=2, reverse=False, colors=[red, orange, blue]),
    ),

    AnimationGroup(
        Pulse(strip3, speed=0.1, color=red),
        Pulse(strip4, speed=0.1, color=red),
        Pulse(strip5, speed=0.1, color=red),
        Pulse(strip6, speed=0.1, color=red),
        Pulse(strip7, speed=0.1, color=red),
        Pulse(strip8, speed=0.1, color=red),
        Pulse(strip9, speed=0.1, color=red),
    ),
    AnimationGroup(
        Rainbow(strip3, speed=0.05, period=5, step=5),
        Rainbow(strip4, speed=0.05, period=5, step=5),
        Rainbow(strip5, speed=0.05, period=5, step=5),
        Rainbow(strip6, speed=0.05, period=5, step=5),
        Rainbow(strip7, speed=0.05, period=5, step=5),
        Rainbow(strip8, speed=0.05, period=5, step=5),
        Rainbow(strip9, speed=0.05, period=5, step=5),
    ),
    AnimationGroup(
        RainbowChase(strip3, speed=0.003, size=1, spacing=0, reverse=False, step=40),
        RainbowChase(strip4, speed=0.003, size=1, spacing=0, reverse=False, step=40),
        RainbowChase(strip5, speed=0.003, size=1, spacing=0, reverse=False, step=40),
        RainbowChase(strip6, speed=0.003, size=1, spacing=0, reverse=False, step=40),
        RainbowChase(strip7, speed=0.003, size=1, spacing=0, reverse=False, step=40),
        RainbowChase(strip8, speed=0.003, size=1, spacing=0, reverse=False, step=40),
        RainbowChase(strip9, speed=0.003, size=1, spacing=0, reverse=False, step=40),
    ),
    AnimationGroup(
        Comet(strip3, speed=0.03, color=(cyan), bounce=True),
        Comet(strip4, speed=0.03, color=(cyan), bounce=True),
        Comet(strip5, speed=0.03, color=(cyan), bounce=True),
        Comet(strip6, speed=0.03, color=(cyan), bounce=True),
        Comet(strip7, speed=0.03, color=(cyan), bounce=True),
        Comet(strip8, speed=0.03, color=(cyan), bounce=True),
        Comet(strip9, speed=0.03, color=(cyan), bounce=True),
    ),
    AnimationGroup(
        RainbowComet(strip3, speed=0.03, tail_length=10, bounce=True),
        RainbowComet(strip4, speed=0.03, tail_length=10, bounce=True),
        RainbowComet(strip5, speed=0.03, tail_length=10, bounce=True),
        RainbowComet(strip6, speed=0.03, tail_length=10, bounce=True),
        RainbowComet(strip7, speed=0.03, tail_length=10, bounce=True),
        RainbowComet(strip8, speed=0.03, tail_length=10, bounce=True),
        RainbowComet(strip9, speed=0.03, tail_length=10, bounce=True),
    ),
    AnimationGroup(
        RainbowSparkle(strip3, speed=0.05, num_sparkles=3),
        RainbowSparkle(strip4, speed=0.05, num_sparkles=3),
        RainbowSparkle(strip5, speed=0.05, num_sparkles=3),
        RainbowSparkle(strip6, speed=0.05, num_sparkles=3),
        RainbowSparkle(strip7, speed=0.05, num_sparkles=3),
        RainbowSparkle(strip8, speed=0.05, num_sparkles=3),
    ),
    AnimationGroup(
        Sparkle(strip3, speed=0.02, color=blue, num_sparkles=3),
        Sparkle(strip4, speed=0.02, color=blue, num_sparkles=3),
        Sparkle(strip5, speed=0.02, color=blue, num_sparkles=3),
        Sparkle(strip6, speed=0.02, color=blue, num_sparkles=3),
        Sparkle(strip7, speed=0.02, color=blue, num_sparkles=3),
        Sparkle(strip8, speed=0.02, color=blue, num_sparkles=3),
        Sparkle(strip9, speed=0.02, color=blue, num_sparkles=3),
    ),
    AnimationGroup(
        SparklePulse(strip3, speed=0.05, color=blue, period=2),
        SparklePulse(strip4, speed=0.05, color=blue, period=2),
        SparklePulse(strip5, speed=0.05, color=blue, period=2),
        SparklePulse(strip6, speed=0.05, color=blue, period=2),
        SparklePulse(strip7, speed=0.05, color=blue, period=2),
        SparklePulse(strip8, speed=0.05, color=blue, period=2),
        SparklePulse(strip9, speed=0.05, color=blue, period=2),
    ),
    AnimationGroup(
        MulticolorComet(strip3, speed=0.04, colors=[red, orange, blue], tail_length=5, bounce=True),
        MulticolorComet(strip4, speed=0.04, colors=[red, orange, blue], tail_length=5, bounce=True),
        MulticolorComet(strip5, speed=0.04, colors=[red, orange, blue], tail_length=5, bounce=True),
        MulticolorComet(strip6, speed=0.04, colors=[red, orange, blue], tail_length=5, bounce=True),
        MulticolorComet(strip7, speed=0.04, colors=[red, orange, blue], tail_length=5, bounce=True),
        MulticolorComet(strip8, speed=0.04, colors=[red, orange, blue], tail_length=5, bounce=True),
        MulticolorComet(strip9, speed=0.04, colors=[red, orange, blue], tail_length=5, bounce=True),
    ),
)

serial_port = usb_cdc.data
serial_port.timeout = 0.1

button_state = False
horn_state = False

while True:
    sequence.animate()
    pressed = not button.value
    if pressed != button_state and pressed:
        print("The button was pressed")
        sequence.next()
    button_state = pressed

    sequence2.animate()
    pressed = not horn.value
    if pressed != horn_state and pressed:
        print("The button was pressed")
        sequence2.next()
    horn_state = pressed

    # Optimized Serial Trigger Implementation
    if serial_port is not None and serial_port.in_waiting > 0:
        # Read the raw bytes and convert to a lowercase string
        line = serial_port.readline().decode().strip().lower()
        
        # Flash a built-in LED or print to test if data is arriving
        if "next_eyes" in line:
            sequence.next()
        elif "next_markings" in line:
            sequence2.next()