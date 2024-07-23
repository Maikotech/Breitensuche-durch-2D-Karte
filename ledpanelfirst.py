#!/usr/bin/python3
import time
import board
import neopixel
pixel_pin = board.D18
num_pixels = 256
#ORDER = neopixel.GRB
pixels1 = neopixel.NeoPixel(pixel_pin, num_pixels)
#unnötig

pixels1.fill((0,0,0))
pixels1[10] = (0,0,255)
pixels1[15] = (0,255,255)
pixels1[20] = (255,0,255)

#def turn_off_leds():
#pixels.fill((0, 0, 0))
 #   pixels[5] = (20, 0, 0)
  #  pixels[5] = (0, 0, 0)
  #  pixels.show()

#turn_off_leds()


def wheel(pos):
 if pos < 0 or pos > 255:
    r = g = b = 0
 elif pos < 85:
    r = int(pos * 3)
    g = int(255 - pos * 3)
    b = 0
 elif pos < 170:
    pos -= 85
    r = int(255 - pos * 3)
    g = 0
    b = int(pos * 3)
 else:
    pos -= 170
    r = 0
    g = int(pos * 3)
    b = int(255 - pos * 3)
 return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def rainbow_cycle(wait):
    for j in range(10):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels)+j
            pixels[i] = wheel(pixel_index & 255)
            pixels.show()
            time.sleep(wait)


print('U256 LED Matrix Module test script')
print('[Press CTRL + C to end the script!]')
try:
    while False:
        print('\nRainbow cycle 1')
        pixels.fill((255, 0, 0))
        pixels.show()
        time.sleep(1)
        print('Rainbow cycle 2')
        pixels.fill((0, 255, 0))
        pixels.show()
        time.sleep(1)
        print('Rainbow cycle 3')
        pixels.fill((0, 0, 255))
        pixels.show()
        time.sleep(1)
        rainbow_cycle(0.001)
except KeyboardInterrupt:
    print('\nScript end!')

