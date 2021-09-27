import pygame 

# Creating the bishop class 
class bishop:
	def __init__(self, x, y, color, square):
		self.x = x 
		self.y = y
		self.square = square
		self.color = color
		if self.color=="black":
			self.bishop = pygame.image.load("img/blackBishop.png")
		else:
			self.bishop = pygame.image.load("img/whiteBishop.png")

		if square!=60:
			self.bishop = pygame.transform.scale(self.bishop, (square, square))

	def draw(self, screen):
		screen.blit(self.bishop, (100+self.x*self.square, 100+self.y*self.square))

	def move(self, pieces, new_pos):
		if (new_pos[1]-self.y)!= 0 and abs((new_pos[0]-self.x)/(new_pos[1]-self.y))==1:
			for piece in pieces:
				if (piece.y-self.y)!=0 and (new_pos[0]-self.x)/(new_pos[1]-self.y)==(piece.x-self.x)/(piece.y-self.y):
					if (new_pos[0]>piece.x and self.x<piece.x) or (new_pos[0]<piece.x and self.x>piece.x):
						return False
			i = 0
			for piece in pieces:
				if piece.x==new_pos[0] and piece.y==new_pos[1]:
					if piece.color==self.color:
						return False
					else:
						del pieces[i]
				i+=1
			self.y=new_pos[1]
			self.x = new_pos[0]
			return True
		return False