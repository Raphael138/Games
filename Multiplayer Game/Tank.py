import pygame
import math

#Tank Class
class Tank:
    def __init__(self, color, x, y):
        self.color = color
        self.health = 10
        self.x = x
        self.y = y
        self.velocity = [3,3]
        self.angle = 0
        if color=="blue":
            self.image = pygame.image.load("img/blueTank.png")
        elif color=="red":
            self.image = pygame.image.load("img/redTank.png")
        self.image = pygame.transform.scale(self.image,(30,30))

    def display(self, screen):
        copy = pygame.transform.rotozoom(self.image, self.angle, 1)
        rect = copy.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center)
        screen.blit(copy,rect.topleft)


    def showHealth(self):
        c = 0
        if self.health>-1:
            for i in range(self.health):
                pygame.draw.rect(screen, (255, 0, 0), (100+c*30, 10, 30, 10))
                c+=1
            for i in range(10-self.health):
                pygame.draw.rect(screen, (255, 0, 0), (100+c*30, 10, 30, 9), width=2)
                c+=1

    def move(self, otherTank):
        keys = pygame.key.get_pressed()
        self.collision()
        if keys[pygame.K_LEFT]:
            self.angle += 5
        if keys[pygame.K_RIGHT]:
            self.angle -= 5
        if keys[pygame.K_UP]:
            self.x += math.cos((self.angle/180)*math.pi)*self.velocity[0]
            self.y -= math.sin((self.angle/180)*math.pi)*self.velocity[1]
            if tankCollision(self,otherTank):
                self.x -= math.cos((self.angle / 180) * math.pi) * self.velocity[0]
                self.y += math.sin((self.angle / 180) * math.pi) * self.velocity[1]
                otherTank.collision()
                otherTank.x += math.cos((self.angle / 180) * math.pi) * otherTank.velocity[0]
                otherTank.y -= math.sin((self.angle / 180) * math.pi) * otherTank.velocity[1]

        if keys[pygame.K_DOWN]:
            self.x -= math.cos((self.angle/180)*math.pi)*self.velocity[0]
            self.y += math.sin((self.angle/180)*math.pi)*self.velocity[1]
            if tankCollision(self,otherTank):
                self.x += math.cos((self.angle / 180) * math.pi) * self.velocity[0]
                self.y -= math.sin((self.angle / 180) * math.pi) * self.velocity[1]
                otherTank.collision()
                otherTank.x -= math.cos((self.angle / 180) * math.pi) * self.velocity[0]
                otherTank.y += math.sin((self.angle / 180) * math.pi) * self.velocity[1]
        self.angle %= 360

    def shoot(self):
        center = self.image.get_rect(topleft=(self.x, self.y)).center
        bullet = Bullet(center[0] + math.cos(((self.angle)/180)*math.pi) * 17, center[1] - math.sin(((self.angle)/180)*math.pi) * 17, self.angle, self.color)
        bullets.append(bullet)
        n.send(make_bullet((bullet.x, bullet.y, bullet.angle, bullet.color)))


    def collision(self):
        rect = self.image.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center)
        if rect.top < 0 :
            self.y+=0.1
            self.velocity[1]=0
            if rect.right> width:
                self.velocity[0] = 0
            elif rect.left < 0:
                self.velocity[0]= 0
        elif rect.bottom>height:
            self.y-=0.1
            self.velocity[1]=0
            if rect.right> width:
                self.velocity[0] = 0
            elif rect.left < 0:
                self.velocity[0]= 0
        elif rect.left < 0 :
            self.x += 0.1
            self.velocity[0] = 0
            if rect.top<0:
                self.velocity[0] = 0
            elif rect.bottom > height:
                self.velocity[0]= 0
        elif rect.right > width:
            self.velocity[0] = 0
            self.x-=0.1
            if rect.top<0:
                self.velocity[0] = 0
            elif rect.bottom > height:
                self.velocity[0]= 0
        else:
            self.velocity[0] = 3
            self.velocity[1] = 3

    def bulletCollision(self, bulletList):
        i = 0
        while (i < len(bulletList)):
            if self.color != bulletList[i].color and bullet_Tank_Collision(self, bulletList[i]):
                self.health -=1
                del bulletList[i]
            i+=1