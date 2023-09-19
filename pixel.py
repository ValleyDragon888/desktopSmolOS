"""
Tools for playing with one NeoPixel LED

(c)2023/07 Krzysztof Krystian Jankowski
Homepage: https://smol.p1x.in/os/
"""

import machine
import neopixel
import time

class Pixel:
    HEARTBEAT_PATTERN = [0, 10, 20, 50, 100, 255, 200, 100, 50, 30, 20, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    BREATHE_DELAY = 0.05
    HEARTBEAT_DELAY = 0.05

    def __init__(self, pin=12):
        self.name = "Pixel"
        # Changes power on pin 11 for XIAO board
        self.power = machine.Pin(11, machine.Pin.OUT)
        self.power.value(1)
        self.pixel = neopixel.NeoPixel(machine.Pin(pin), 1)
        self.msg("Initialized.")
            
    def msg(self, message):
        print(f"{self.name} : {message}")
        
    def color(self, color=((0,0,0))):
        self.pixel.fill(color)
        self.pixel.write()
        self.msg(f"Color set to: \n\t* Red {color[0]}\n\t* Green {color[1]}\n\t* Blue {color[2]}")

    def heartbeat(self):
        """
        Animate the NeoPixel with a "heartbeat" pattern.
        """
        self.msg("Press Ctrl+C to quit.\n")
        while True:
            try:
                for brightness in self.HEARTBEAT_PATTERN:
                    red = int((255 * brightness) / 255)
                    green = int((105 * brightness) / 255)
                    blue = int((180 * brightness) / 255)
                    self.pixel.fill((red, red, red))
                    self.pixel.write()
                    time.sleep(self.HEARTBEAT_DELAY)
            except KeyboardInterrupt:
                break

    def breath(self):
        """
        Animate the NeoPixel with a "breath" pattern.
        """
        self.msg("Press Ctrl+C to quit.\n")
        while True:
            try:
                for brightness in range(255):
                    white = int((255 * brightness) / 255)
                    self.pixel.fill((white, white, white))
                    self.pixel.write()
                    time.sleep(self.BREATHE_DELAY)
                time.sleep(1)
                for brightness in range(255):
                    white = 255 - int((255 * brightness) / 255)
                    self.pixel.fill((white, white, white))
                    self.pixel.write()
                    time.sleep(self.BREATHE_DELAY)
            except KeyboardInterrupt:
                break

    def run(self, color=(64, 64, 255)):
        if type(color) is tuple:
             self.color(color)
        else:
            self.msg("Wrong color argument. Expected format: (0,0,0)\n")
        

if __name__ == '__main__':
    pixel = Pixel()
    pixel.run()

