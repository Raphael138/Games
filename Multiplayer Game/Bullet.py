import pygame
import math

#Bullet class
class Bullet:
    def __init__(self, x, y, angle, color):
        self.color = color
        self.x = x
        self.y = y
        self.angle = angle
        self.image = pygame.image.load("img/bulletimg.png")
        self.image = pygame.transform.rotozoom(self.image, self.angle,0.018)

    def draw(self, screen):
        self.x += math.cos((self.angle/180)*math.pi)*6
        self.y -= math.sin((self.angle / 180) * math.pi)*6
        screen.blit(self.image, (self.x-self.image.get_width()/2, self.y-self.image.get_height()/2))

    def check(self):
        if self.x>width  or self.x<0 or self.y>height or self.y<0:
            return True
        else:
            return False
