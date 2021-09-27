import pygame
import math
import time
from network import Network

#List of all the bullets
bullets = []

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
            # if tankCollision(self,otherTank):
            #     self.x -= math.cos((self.angle / 180) * math.pi) * self.velocity[0]
            #     self.y += math.sin((self.angle / 180) * math.pi) * self.velocity[1]
            #     otherTank.collision()
            #     otherTank.x += math.cos((self.angle / 180) * math.pi) * otherTank.velocity[0]
            #     otherTank.y -= math.sin((self.angle / 180) * math.pi) * otherTank.velocity[1]

        if keys[pygame.K_DOWN]:
            self.x -= math.cos((self.angle/180)*math.pi)*self.velocity[0]
            self.y += math.sin((self.angle/180)*math.pi)*self.velocity[1]
            # if tankCollision(self,otherTank):
            #     self.x += math.cos((self.angle / 180) * math.pi) * self.velocity[0]
            #     self.y -= math.sin((self.angle / 180) * math.pi) * self.velocity[1]
            #     otherTank.collision()
            #     otherTank.x -= math.cos((self.angle / 180) * math.pi) * otherTank.velocity[0]
            #     otherTank.y += math.sin((self.angle / 180) * math.pi) * otherTank.velocity[1]
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


################################################################################################################################################################################################################################


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


################################################################################################################################################################################################################


def updatingBullets(bulletList):
    i = 0
    while (i < len(bulletList)):
        bulletList[i].draw(screen)
        if bulletList[i].check():
            del bulletList[i]
        i += 1

def tankCollision(tank1, tank2):
    tank1_mask = pygame.mask.from_surface(pygame.transform.rotozoom(tank1.image, tank1.angle, 1))
    tank2_mask = pygame.mask.from_surface(pygame.transform.rotozoom(tank2.image, tank2.angle, 1))

    offset_x = round(tank1.x - tank2.x)
    offset_y = round(tank1.y - tank2.y)

    overlap = tank1_mask.overlap(tank2_mask, (offset_x, offset_y))

    
    if overlap:
        return True

    return False

#Collision of tank and bullets
def bullet_Tank_Collision(tank, bullet):
    tank_center = tank.image.get_rect(topleft=(tank.x, tank.y)).center
    angle_x = tank.angle%90-45
    angle_y = tank.angle%90+45

    tank_l_x, tank_r_x  = tank_center[0]-21.2132*math.cos(math.pi*(angle_x)/180), tank_center[0]+21.2132*math.cos(math.pi*(angle_x)/180)
    tank_t_y, tank_b_y = tank_center[1]-21.2132*math.sin(math.pi*(angle_y)/180), tank_center[1]+21.2132*math.sin(math.pi*(angle_y)/180)

    end_x, end_y = bullet.x+9*math.cos(math.pi*(bullet.angle)/180), bullet.y-9*math.sin(math.pi*(bullet.angle)/180)

    # Note: Because I have yet to try this with the red tank turned, I may need to edit this code to take that into account

    if end_x>tank_l_x and end_x<tank_r_x:
        if end_y>tank_t_y and end_y<tank_b_y:
            return True
    return False

def read_data(str):
    str = str.split(":")
    if len(str)>1:
        temp = str[0].split("b")[0]
        temp = temp.split(",")
        return float(temp[0]), float(temp[1]), float(temp[2]), read_bullet(str[1])
    str = str[0].split(",")
    return float(str[0]), float(str[1]), float(str[2])

def make_tank(tup):
    return str(round(tup[0], 3))+","+str(round(tup[1], 3))+","+str(tup[2])

def make_bullet(tup):
    return "bullet:"+str(round(tup[0], 3))+","+str(round(tup[1], 3))+","+str(tup[2])+","+tup[3]

def read_bullet(str):
    str = str.split(",")
    return float(str[0]), float(str[1]), float(str[2]), str[3]

#Starting the game
height, width = 500,500
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((height, width))

n = Network()
starting_data = read_data(n.getPos())

#Loading the red tank and blue tank
blueTank = Tank("blue", starting_data[0],starting_data[1])
blueTank.angle = starting_data[2]
redTank = Tank("red", 250, 250)

#Main loop
run = True
while run:
    #Resetting screen
    screen.fill((255,255,255))

    #Getting the redtank position and sending our position
    sending_data = (blueTank.x, blueTank.y, blueTank.angle)
    receivedData = (read_data(n.send(make_tank(sending_data))))
    redTank.x = receivedData[0]
    redTank.y = receivedData[1]
    redTank.angle = receivedData[2]
    if len(receivedData)>3:
        b_data = receivedData[3]
        bullets.append(Bullet(b_data[0], b_data[1], b_data[2], b_data[3]))

    #Drawing the tank
    blueTank.display(screen)
    redTank.display(screen)
    blueTank.move(redTank)
    redTank.bulletCollision(bullets)
    blueTank.bulletCollision(bullets)
    redTank.showHealth()

    #Drawing the bullets
    updatingBullets(bullets)

    # Screen updating
    clock.tick(60)
    pygame.display.flip()

    #Looking for keypress and quiting if needed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                blueTank.shoot()