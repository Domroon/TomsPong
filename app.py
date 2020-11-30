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


def load_sound(name):
    class NoneSound:
        def play(self):
            pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join("data", name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print('Cannot load sound:', fullname)
        raise SystemExit(message)
    return sound


# Game object classes
class Ball(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    FUnctions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('ball.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect, self.vector)
        self.rect = newpos

    def calcnewpos(self, rect, vector):
        (angle, z) = vector
        (dx, dy) = (z*math.cos(angle), z*math.sin(angle))
        return rect.move(dx, dy)

# Any other game functions
# Initialise the game
# The main loop
def main():
    # testing
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    ball = Ball((10, 10))


if __name__ == "__main__":
    main()
