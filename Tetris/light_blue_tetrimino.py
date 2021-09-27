import pygame

#creating light blue block class
class light_blue_tetrimino:
    def __init__(self,x ,y, position, pix_size):
        self.x = x
        self.y = y
        self.color = "light blue"
        self.position = position
        self.light_blue_block = pygame.image.load('img/light_blue_pixel.png')
        self.pixel_size = pix_size

    def draw(self, screen):
        if self.position==0:
            for i in range(0,4):
                screen.blit(self.light_blue_block, (self.x*self.pixel_size+50+i*self.pixel_size, (self.y+1)*self.pixel_size+100))
        elif self.position==1:
            for i in range(0, 4):
                screen.blit(self.light_blue_block, ((self.x+2)*self.pixel_size+50, (self.y)*self.pixel_size+100 + i * self.pixel_size))
        elif self.position==2:
            for i in range(0,4):
                screen.blit(self.light_blue_block, (self.x*self.pixel_size+50+i*self.pixel_size, (self.y+2)*self.pixel_size+100))
        elif self.position==3:
            for i in range(0, 4):
                screen.blit(self.light_blue_block, ((self.x+1)*self.pixel_size+50, (self.y)*self.pixel_size+100 + i * self.pixel_size))

    def getPosition(self):
        o = []
        if self.color=="light blue":
            if self.position==0:
                for i in range(4):
                    o.append((self.y+1,self.x+i))
            elif self.position==1:
                for i in range(4):
                    o.append((self.y+i,self.x+2))
            elif self.position==2:
                for i in range(4):
                    o.append((self.y+2,self.x+i))
            elif self.position==3:
                for i in range(4):
                    o.append((self.y+i,self.x+1))
        return o

    def determine(self, event, grid):
        if event.key == pygame.K_UP:
            self.position +=1
            tempPos = self.getPosition()
            turnBack = False
            for i in tempPos:
                if i[1]<0 or i[1]>9:
                    turnBack=True
                    break
            if turnBack or self.collision(grid):
                self.position-=1
            self.position%=4
        if event.key == pygame.K_DOWN:
            self.y +=1
        if event.key == pygame.K_RIGHT:
            self.x +=1
            tempPos = self.getPosition()
            turnBack = False
            for i in tempPos:
                if i[1]<0 or i[1]>9:
                    turnBack=True
                    break
            if turnBack or self.collision(grid):
                self.x-=1
        if event.key == pygame.K_LEFT:
            self.x -=1
            tempPos = self.getPosition()
            turnBack = False
            for i in tempPos:
                if i[1]<0 or i[1]>9:
                    turnBack=True
                    break
            if turnBack or self.collision(grid):
                self.x+=1

    def collision(self, grid):
        self.y+=1
        pos1 = self.getPosition()
        self.y-=1
        for i in range(len(pos1)):
            if pos1[i][0]>19:
                return True
            elif grid.mat[pos1[i][0]][pos1[i][1]]!=0:
                return True

        return False

