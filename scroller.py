import machine
import time
import neopixel
import math
from font import Font

BLANK_COLOR = (0,0,0)
BACKGROUND_COLOR = (0,0,0)
FORGROUND_COLOR = (64,12,12)
DELEAY=0.08
PAUSE=0.12
SCREEN_LEN=5*5

class Scroller():
    def __init__(self):
        self.pixels = neopixel.NeoPixel(machine.Pin(29),SCREEN_LEN)
        self.pixels.fill((0,0,0))
        self.pixels.write()
        self.font = Font()
        self.logging = False

    def draw(self,bitmap,offset=0):
        pixel_color = BACKGROUND_COLOR
        for i in range(25):
            if i+offset<0 or i+offset>len(bitmap)-1:
                pixel_color=BACKGROUND_COLOR
            else:
                if bitmap[i+offset]:
                    pixel_color=FORGROUND_COLOR
                else:
                   pixel_color=BACKGROUND_COLOR
            self.pixels[24-i]=pixel_color
        self.pixels.write()

    def get_word_bitmap(self, word):
        out_glyf = []
        for letter in word:
            out_glyf += self.font.get_glyf_bitmap(letter.lower())
        return out_glyf

    def log(self, log):
        if self.logging:
            print(log)

    def draw_text(self, text=""):
        if text=="":
            return
        self.log(f"Scrolling text: {text}")
        self.log("Press Ctrl+C to quit.\n")
        for word in text.split(' '):
            self.marquee(self.get_word_bitmap(word))

    def marquee(self,bitmap,loop=False):
        offset=-SCREEN_LEN
        bit_len=len(bitmap)
        while True:
            self.draw(bitmap,offset)
            if offset==0 and bit_len == SCREEN_LEN:
                time.sleep(PAUSE)
            else:
                time.sleep(DELEAY)
            offset += 5
            if offset > bit_len:
                offset=-SCREEN_LEN
                if not loop:
                    return

    def run(self, message="Specialized Microcontroller-Oriented Lightweight Operating System"):
        self.draw_text(message)

if __name__ == '__main__':
    scroller = Scroller()
    scroller.logging = True
    scroller.run()

