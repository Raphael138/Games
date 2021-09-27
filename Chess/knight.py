import pygame 

# Creating the knight class 
class knight:
	def __init__(self, x, y, color, square):
		self.x = x 
		self.y = y
		self.color = color
		self.square = square
		if self.color=="black":
			self.knight = pygame.image.load("img/blackKnight.png")
		else:
			self.knight = pygame.image.load("img/whiteKnight.png")

		if square!=60:
			self.knight = pygame.transform.scale(self.knight, (square, square))

	def draw(self, screen):
		screen.blit(self.knight, (100+self.x*self.square, 100+self.y*self.square))

	def move(self, pieces, new_pos):
		if ((new_pos[0]==self.x+1 or new_pos[0]==self.x-1) and (new_pos[1]==self.y-2 or new_pos[1]==self.y+2)) or ((new_pos[0]==self.x+2 or new_pos[0]==self.x-2) and (new_pos[1]==self.y-1 or new_pos[1]==self.y+1)):
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