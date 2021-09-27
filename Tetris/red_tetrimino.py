import pygame

#defining the red tetris block class
class red_tetrimino:
    def __init__(self,x,y, position, pix_size):
        self.x = x
        self.y = y
        self.color = "red"
        self.position = position
        self.red_block = pygame.image.load('img/red_pixel.png')
        self.pixel_size = pix_size

    def draw(self, screen):
        if self.position==0:
            for i in range(-1,1):
                screen.blit(self.red_block, (50+self.x*self.pixel_size+i*self.pixel_size, 100+(self.y-1)*self.pixel_size))
            for i in range(0,2):
                screen.blit(self.red_block, (50+self.x*self.pixel_size+i*self.pixel_size, 100+(self.y)*self.pixel_size))
        elif self.position==1:
            for i in range(-1,1):
                screen.blit(self.red_block, (50+(self.x+1)*self.pixel_size, 100+(self.y)*self.pixel_size+i*self.pixel_size))
            for i in range(0,2):
                screen.blit(self.red_block, (50+(self.x)*self.pixel_size, 100+(self.y)*self.pixel_size+i*self.pixel_size))
        elif self.position==2:
            for i in range(-1,1):
                screen.blit(self.red_block, (50+self.x*self.pixel_size+i*self.pixel_size, 100+(self.y)*self.pixel_size))
            for i in range(0,2):
                screen.blit(self.red_block, (50+self.x*self.pixel_size+i*self.pixel_size, 100+(self.y+1)*self.pixel_size))
        elif self.position==3:
            for i in range(-1,1):
                screen.blit(self.red_block, (50+(self.x)*self.pixel_size, 100+self.y*self.pixel_size+i*self.pixel_size))
            for i in range(0,2):
                screen.blit(self.red_block, (50+(self.x-1)*self.pixel_size, 100+self.y*self.pixel_size+i*self.pixel_size))

    def getPosition(self):
        o = []
        if self.color=="red":
            if self.position==0:
                for i in range(-1,1):
                    o.append((self.y-1,self.x+i))
                for i in range(0,2):
                    o.append((self.y,self.x+i))
            elif self.position==1:
                for i in range(-1,1):
                    o.append((self.y+i,self.x+1))
                for i in range(0,2):
                    o.append((self.y+i,self.x))
            elif self.position==2:
                for i in range(-1,1):
                    o.append((self.y,self.x+i))
                for i in range(0,2):
                    o.append((self.y+1,self.x+i))
            elif self.position==3:
                for i in range(-1,1):
                    o.append((self.y+i,self.x))
                for i in range(0,2):
                    o.append((self.y+i,self.x-1))
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

