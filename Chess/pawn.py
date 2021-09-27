import pygame 

# Creating the pawn class 
class pawn:
	def __init__(self, x, y, color, square):
		self.x = x 
		self.y = y
		self.square = square
		self.first_move = False
		self.color = color
		if self.color=="black":
			self.pawn = pygame.image.load("img/blackPawn.png")
		else:
			self.pawn = pygame.image.load("img/whitePawn.png")

		if square!=60:
			self.pawn = pygame.transform.scale(self.pawn, (square, square))

	def draw(self, screen):
		screen.blit(self.pawn, (100+self.x*self.square, 100+self.y*self.square))

	def move(self, pieces, new_pos):
		if new_pos[0]==self.x and self.color=="white" and new_pos[1]==self.y-1:
			for piece in pieces:
				if piece.x==new_pos[0] and piece.y==new_pos[1]:
					return False
			self.y=new_pos[1]
			self.first_move = True
			return True
		elif new_pos[0]==self.x and self.color=="white" and new_pos[1]==self.y-2 and not self.first_move:
			for piece in pieces:
				if piece.x==new_pos[0] and (piece.y==new_pos[1] or piece.y==new_pos[1]+1):
					return False
			self.y=new_pos[1]
			self.first_move = True
			return True
		elif new_pos[0]==self.x and self.color=="black" and new_pos[1]==self.y+1:
			for piece in pieces:
				if piece.x==new_pos[0] and piece.y==new_pos[1]:
					return False
			self.y=new_pos[1]
			self.first_move = True
			return True
		elif new_pos[0]==self.x and self.color=="black" and new_pos[1]==self.y+2 and not self.first_move:
			for piece in pieces:
				if piece.x==new_pos[0] and (piece.y==new_pos[1] or piece.y==new_pos[1]-1):
					return False
			self.y=new_pos[1]
			self.first_move = True
			return True
		elif (new_pos[0]==self.x+1 or new_pos[0]==self.x-1) and self.color=="white" and new_pos[1]==self.y-1:
			i = 0
			for piece in pieces:
				if piece.color!=self.color:
					if piece.x==new_pos[0] and piece.y==new_pos[1]:
						self.y=new_pos[1]
						self.x=new_pos[0]
						self.first_move = True
						del pieces[i]
						return True
				i+=1
			return False
		elif (new_pos[0]==self.x+1 or new_pos[0]==self.x-1) and self.color=="black" and new_pos[1]==self.y+1:
			i = 0
			for piece in pieces:
				if piece.color!=self.color:
					if piece.x==new_pos[0] and piece.y==new_pos[1]:
						self.y=new_pos[1]
						self.x=new_pos[0]
						self.first_move = True
						del pieces[i]
						return True
				i+=1
			return False
		return False

	def checkForUpgrade(self):
		if self.color=="white" and self.y==0:
			return True
		elif self.color=="black" and self.y==7:
			return True