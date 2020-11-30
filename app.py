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


class Bat(pygame.sprite.Sprite):
    """Movable tennis 'bat' with one hits the ball
    Returns: bat object
    Functions: reinit, update, moveup, movedown
    Attributes: which, speed"""

    def __init__(self, side):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('bat.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.side = side
        self.speed = 10
        self.state = "still"
        self.reinit()

    def reinit(self):
        self.state = "still"
        self.movepos = [0, 0]
        if self.side == "left":
            self.rect.midleft = self.area.midleft
        elif self.side == "right":
            self.rect.midright = self.area.midright

    def update(self):
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        pygame.event.pump()

    def moveup(self):
        self.movepos[1] = self.movepos[1] - self.speed
        self.state = "moveup"

    def movedown(self):
        self.movepos[1] = self.movepos[1] + self.speed
        self.state = "movedown"
# Any other game functions
# -


def main():
    # Initialise the game
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    ball = Ball((10, -2))
    player = Bat('left')
    clock = pygame.time.Clock()
    allsprites = pygame.sprite.RenderPlain(ball, player)

    # The main loop
    run = True
    game_speed = 60
    while run:
        clock.tick(game_speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    player.moveup()
                if event.key == K_DOWN:
                    player.movedown()
            elif event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    player.movepos = [0, 0]
                    player.state = "still"

        ball.update()
        player.update()
        allsprites.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
