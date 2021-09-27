import pygame 

# Creating the rook class 
class rook:
	def __init__(self, x, y, color, square):
		self.x = x 
		self.y = y
		self.square = square
		self.color = color
		if self.color=="black":
			self.rook = pygame.image.load("img/blackRook.png")
		else:
			self.rook = pygame.image.load("img/whiteRook.png")

		if square!=60:
			self.rook = pygame.transform.scale(self.rook, (square, square))

	def draw(self, screen):
		screen.blit(self.rook, (100+self.x*self.square, 100+self.y*self.square))

	def move(self, pieces, new_pos):
		if (self.x==new_pos[0] and self.y!=new_pos[1]):
			for piece in pieces:
				if piece.x==self.x:
					if (new_pos[1]>piece.y and self.y<piece.y) or (new_pos[1]<piece.y and self.y>piece.y):
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
		elif (self.x!=new_pos[0] and self.y==new_pos[1]):
			for piece in pieces:
				if piece.y==self.y:
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