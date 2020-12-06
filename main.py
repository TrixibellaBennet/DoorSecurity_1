# Drive NeoPixels on the NeoPixels Block on Crickit for
#  Circuit Playground Express
import time
import neopixel
import board
from adafruit_circuitplayground import cp
#from adafruit_crickit import crickit


num_pixels = 30  # Number of pixels driven from Crickit NeoPixel terminal

# The following line sets up a NeoPixel strip on Crickit CPX pin A1
pixels = neopixel.NeoPixel(board.A1, num_pixels, brightness=1,
                           auto_write=False)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def color_chase(color):
    for i in range(num_pixels):
        pixels[i] = color
    pixels.show()

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

while True:
    #color_chase((0, 0, 0), 0.001)
    if cp.touch_A2:
        color_chase(RED)
        #rainbow_cycle(0)  # Increase the number to slow down the rainbow
    if cp.touch_A3:
        color_chase(WHITE)
    if cp.touch_A7:
        color_chase(BLACK)
    else:
        color_chase(BLACK)