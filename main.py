#!/usr/bin/env python3
import os
from dotenv import load_dotenv

from gif_viewer import GifViewer

if __name__ == "__main__":
    load_dotenv()

    gif = os.getenv("GIF")

    gif_viewer = GifViewer(gif)
    gif_viewer.run()
