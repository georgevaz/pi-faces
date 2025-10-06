#!/usr/bin/env python3
import os
from dotenv import load_dotenv

from ollama_request import sendRequest
# from gif_viewer import GifViewer

if __name__ == "__main__":
    # load_dotenv()

    # gif = os.getenv("GIF")

    # gif_viewer = GifViewer(gif)
    # gif_viewer.run()


    try:
        active = True
        while(active):
            user_input = input("Enter prompt: ")
            if user_input == "quit":
                print("Closing session.")
                active = False
                continue
            try:
                sendRequest(user_input)
            except ValueError as e:
                print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nEnd session")