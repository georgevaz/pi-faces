#!/usr/bin/env python
import time
import sys

from PIL import Image
from matrix_config import matrix

class GifViewer():
    def __init__(self, image_file, run_time=float('inf')):
        self.image_file = image_file
        self.run_time = run_time # in seconds, infinity by default
        self.canvases = []
        self.num_frames = 0

    def preprocess(self):
        gif = Image.open(self.image_file)

        try:
            self.num_frames = gif.n_frames
        except Exception:
            sys.exit("provided image is not a gif")

        # Preprocess the gifs frames into canvases to improve playback performance
        print("Preprocessing gif, this may take a moment depending on the size of the gif...")
        for frame_index in range(0, self.num_frames):
            gif.seek(frame_index)
            # must copy the frame out of the gif, since thumbnail() modifies the image in-place
            frame = gif.copy()
            frame.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
            canvas = matrix.CreateFrameCanvas()
            canvas.SetImage(frame.convert("RGB"))
            self.canvases.append(canvas)
        # Close the gif file to save memory now that we have copied out all of the frames
        gif.close()

        print("Completed Preprocessing, displaying gif")

    def run(self):
        if not self.image_file:
            sys.exit("Require a gif argument")

        # Preprocess the gif if it hasn't be done already
        if len(self.canvases) <= 0:
            self.preprocess()

        try:
            print("Press CTRL-C to stop.")

            # Infinitely loop through the gif
            cur_frame = 0
            end_time = time.time() + self.run_time

            while time.time() <= end_time:
                matrix.SwapOnVSync(self.canvases[cur_frame], framerate_fraction=10)
                if cur_frame == self.num_frames - 1:
                    cur_frame = 0
                else:
                    cur_frame += 1
        except KeyboardInterrupt:
            sys.exit(0)

# main function
if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Requires a gif argument")
    gif_viewer = GifViewer(sys.argv[1])
    if not gif_viewer.run():
        sys.exit("Unable to run")
