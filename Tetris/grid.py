import pygame 

#creating a grid class which will help with collision
class Grid:
    def __init__(self, cols, rows, pixel_size):
        self.mat = [[0 for i in range(cols)]for j in range(rows+1)]
        self.pixel_size = pixel_size

    def update(self, tetromino):
        for i in tetromino.getPosition():
            if tetromino.color=="blue":
                self.mat[i[0]][i[1]]=tetromino.blue_block
            elif tetromino.color=="green":
                self.mat[i[0]][i[1]]=tetromino.green_block
            elif tetromino.color=="light blue":
                self.mat[i[0]][i[1]]=tetromino.light_blue_block
            elif tetromino.color=="orange":
                self.mat[i[0]][i[1]]=tetromino.orange_block
            elif tetromino.color=="purple":
                self.mat[i[0]][i[1]]=tetromino.purple_block
            elif tetromino.color=="red":
                self.mat[i[0]][i[1]]=tetromino.red_block
            else:
                self.mat[i[0]][i[1]]=tetromino.yellow_block
            
    #     self.checkRows()

    # def checkRows(self):
    #     for i in self.mat:
    #         c = 0
    #         for j in i:
    #             if j==1:
    #                 c+=1

    #         if c==len(i):
    
    def draw(self, screen):
        colid = 0
        for i in self.mat:
            rowid = 0
            for j in i:
                if j!=0:
                    screen.blit(j, (50+(rowid+1)*self.pixel_size, 100 + (colid-1)*self.pixel_size)) 
                rowid+=1
            colid+=1