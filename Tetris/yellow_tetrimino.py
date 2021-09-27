import pygame

#creating yellow block class
class yellow_tetrimino:
    def __init__(self,x,y, pix_size):
        self.x = x
        self.y = y
        self.color = "yellow"
        self.yellow_block = pygame.image.load('img/yellow_pixel.png')
        self.pixel_size = pix_size

    def draw(self, screen):
        for i in range(0,2):
            screen.blit(self.yellow_block,(50+self.x*self.pixel_size+i*self.pixel_size, 100+self.y*self.pixel_size))
        for i in range(0,2):
            screen.blit(self.yellow_block,(50+self.x*self.pixel_size+i*self.pixel_size, 100+(self.y+1)*self.pixel_size))

    def getPosition(self):
        o = []
        for i in range(2):
            o.append((self.y,self.x+i))
        for i in range(2):
            o.append((self.y+1,self.x+i))
        return o

    def determine(self, event, grid):
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
