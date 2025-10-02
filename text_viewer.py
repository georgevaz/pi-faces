#!/user/bin/env python
import sys
from rgbmatrix import graphics
from matrix_config import matrix

class TextViewer():
    def __init__(self, text="Hello World"):
        self.text = text

    def run(self):
        canvas = matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("./fonts/7x13.bdf")
        text_color = graphics.Color(255, 255, 0)
        pos = 0

        print("Running text...")
        while True:
            canvas.Clear()
            len = graphics.DrawText(canvas, font, pos, 10, text_color, self.text)
            canvas = matrix.SwapOnVSync(canvas)

if __name__ == "__main__":
    text_viewer = TextViewer()
    if not text_viewer.run():
        sys.exit("Unable to run")
