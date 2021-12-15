import pygame, sys, math

class HUD():
    def __init__(self, startPos=[0,0]):
        font = pygame.font.Font(None, 36)
        text = font.render("Score: 0", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text, textpos)
