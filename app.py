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
def load_png(name):
    """Load image and return image object"""
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print('cannot load image:', image)
        raise (SystemExit, message)
    return image, image.get_rect()

# Game object classes
# Any other game functions
# Initialise the game
# The main loop
