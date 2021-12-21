import pygame, sys, math
from Ball import *

class PlayerBall(Ball):
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        Ball.__init__(self, [0,0], startPos)
        self.imagesUp = [pygame.image.load("images\playerball\playerBall-up.png")]
        self.imagesDown = [pygame.image.load("images\playerball\playerBall-down.png")]
        self.imagesLeft = [pygame.image.load("images\playerball\playerBall-left.png")]
        self.imagesRight = [pygame.image.load("images\playerball\playerBall-right.png")]
        self.images = self.imagesUp
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.maxSpeed = maxSpeed
        self.kind = "player"
        
    def goKey(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
            self.images = self.imagesLeft
        elif direction == "right":
            self.speedx = self.maxSpeed
            self.images = self.imagesRight
        elif direction == "up":
            self.speedy = -self.maxSpeed
            self.images = self.imagesUp
        elif direction == "down":
            self.speedy = self.maxSpeed
            self.images = self.imagesDown
        elif direction == "sleft":
            self.speedx = 0
        elif direction == "sright":
            self.speedx = 0
        elif direction == "sup":
            self.speedy = 0
        elif direction == "sdown":
            self.speedy = 0
        self.image = self.images[0]
        
    def update(self, size):
        self.move()
        self.wallCollide(size)
            
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if self.rect.bottom > height:
            self.speedy = -self.speedy
            self.move()
            self.speedy = 0
        if self.rect.top < 0:
            self.speedy = -self.speedy
            self.move()
            self.speedy = 0
        
        
        if self.rect.right > width:
            self.speedx = -self.speedx
            self.move()
            self.speedx = 0
        if self.rect.left < 0:
            self.speedx = -self.speedx
            self.move()
            self.speedx = 0
            
    def ballCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                return True
        return False
