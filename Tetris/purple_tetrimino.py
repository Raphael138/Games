import pygame

#defining the purple tetris block class
class purple_tetrimino:
    def __init__(self,x,y,position, pix_size):
        self.x = x
        self.y = y
        self.color = "purple"
        self.position = position
        self.purple_block = pygame. image.load('img/purple_pixel.png')
        self.pixel_size = pix_size

    def draw(self, screen):
        if self.position == 0:
            for i in range(-1,2):
                screen.blit(self.purple_block, (50+self.x*self.pixel_size+i*self.pixel_size, 100+(self.y)*self.pixel_size))
            screen.blit(self.purple_block, (50+(self.x)*self.pixel_size, 100+(self.y-1)*self.pixel_size))
        if self.position == 1:
            for i in range(-1,2):
                screen.blit(self.purple_block, (50+(self.x)*self.pixel_size, 100+self.y*self.pixel_size+i*self.pixel_size))
            screen.blit(self.purple_block, (50+(self.x+1)*self.pixel_size, 100+(self.y)*self.pixel_size))
        if self.position == 2:
            for i in range(-1,2):
                screen.blit(self.purple_block, (50+self.x*self.pixel_size+i*self.pixel_size, 100+(self.y)*self.pixel_size))
            screen.blit(self.purple_block, (50+(self.x)*self.pixel_size, 100+(self.y+1)*self.pixel_size))
        if self.position == 3:
            for i in range(-1,2):
                screen.blit(self.purple_block, (50+(self.x)*self.pixel_size, 100+self.y*self.pixel_size+i*self.pixel_size))
            screen.blit(self.purple_block, (50+(self.x-1)*self.pixel_size, 100+(self.y)*self.pixel_size))
    
    def getPosition(self):
        o = []
        if self.color=="purple":
            if self.position==0:
                o.append((self.y-1,self.x))
                for i in range(-1,2):
                    o.append((self.y,self.x+i))
            elif self.position==1:
                o.append((self.y,self.x+1))
                for i in range(-1,2):
                    o.append((self.y+i,self.x))
            elif self.position==2:
                o.append((self.y+1,self.x))
                for i in range(-1,2):
                    o.append((self.y,self.x+i))
            elif self.position==3:
                o.append((self.y,self.x-1))
                for i in range(-1,2):
                    o.append((self.y+i,self.x))
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

