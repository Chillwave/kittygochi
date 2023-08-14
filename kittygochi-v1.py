import os
import time
import random

class ASCIIAnimationEngineRandom:
    def __init__(self, files):
        self.frames = {name: self.read_file(filename) for name, filename in files.items()}
        self.position = 20  # Starting position for the ASCII art on the screen
        self.direction = 1  # 1 for moving right, -1 for moving left

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def read_file(self, filename):
        with open(filename, 'r') as file:
            return file.read()

    def display_frame(self, frame_name):
        frame = self.frames[frame_name]
        print(" " * self.position + frame.replace("\n", "\n" + " " * self.position))

    def animate_random(self, duration):
        animation_sequence = list(self.frames.keys())
        while True:
            frame_name = random.choice(animation_sequence)
            self.clear_screen()
            self.display_frame(frame_name)
            time.sleep(duration)
            self.move_position()

    def move_position(self):
        self.position += self.direction * 2
        if self.position > 40 or self.position < 10:
            self.direction *= -1  # Change direction

if __name__ == "__main__":
    files = {
        'open_eyes': 'cat_open_eyes.txt',
        'closed_eyes': 'cat_closed_eyes.txt',
        'poker_face': 'cat_poker_face.txt',
        'sad': 'cat_sad.txt',
        'blank': 'cat_blank.txt',
        'staring': 'cat_staring.txt',
    }

    engine = ASCIIAnimationEngineRandom(files)
    engine.animate_random(0.5)
