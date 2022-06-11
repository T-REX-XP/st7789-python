#!/usr/bin/env python3
from ST7789 import ST7789, BG_SPI_CS_FRONT
from PIL import Image, ImageDraw

import random
import time

# Buttons
BUTTON_A = 5
BUTTON_B = 6
BUTTON_X = 16
BUTTON_Y = 24

# Onboard RGB LED
LED_R = 17
LED_G = 27
LED_B = 22

# General
SPI_PORT = 1
SPI_CS = 24
SPI_DC = 22
BACKLIGHT = 18

# Screen dimensions
WIDTH = 240
HEIGHT = 240

buffer = Image.new("RGB", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(buffer)

draw.rectangle((0, 0, 50, 50), (255, 0, 0))
draw.rectangle((240-50, 0, 240, 50), (0, 255, 0))
draw.rectangle((0, 240-50, 50, 240), (0, 0, 255))
draw.rectangle((240-50, 240-50, 240, 240), (255, 255, 0))

display = ST7789(
    port=SPI_PORT,
    cs=SPI_CS,
    dc=SPI_DC,
    backlight=BACKLIGHT,
    width=WIDTH,
    height=HEIGHT,
    rotation=180,
    spi_speed_hz=10 * 1000 * 1000
)

while True:
    display.display(buffer)
    time.sleep(1.0 / 60)