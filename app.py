#!/usr/bin/env python
#
# Tom's Pong
# A simple pong game with realistic physics and AI
#
# Released under the GNU General Public License

VERSION = "0.4"

# Load modules
try:
    import sys
    import random
    import math
    import os
    import getopt
    from socket import *
    from pygame.locals import *
    import pygame
except ImportError as err:
    print("couldn't load module:", err)
    sys.exit(2)


# Resource handling classes/functions
def load_image(name, colorkey=None):
    fullname = os.path.join("data", name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image: ', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

# Game object classes
# Any other game functions
# Initialise the game
# The main loop
def main():
    # testing
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    print(os.path.join("c:", "data"))
    testIMG = load_image('chimp.jpg')
    testIMG2 = load_image('triangle.png')


if __name__ == "__main__":
    main()
