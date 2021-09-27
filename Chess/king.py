import pygame 
from rook import rook

# Creating the king class 
class king:
	def __init__(self, x, y, color, square):
		self.x = x 
		self.y = y
		self.color = color
		self.first_move = False
		self.square = square
		if self.color=="black":
			self.king = pygame.image.load("img/blackKing.png")
		else:
			self.king = pygame.image.load("img/whiteKing.png")

		if square!=60:
			self.king = pygame.transform.scale(self.king, (square, square))

	def draw(self, screen):
		screen.blit(self.king, (100+self.x*self.square, 100+self.y*self.square))

	def move(self, pieces, new_pos):
		if not self.first_move:
			if new_pos[0]==6 and new_pos[1]==7:
				rook_index = -1
				i=0
				for piece in pieces:
					if piece.y==7 and (piece.x==6 or piece.x==5):
						return False
					elif piece.y==7 and piece.x==7 and type(piece)==rook and self.color==piece.color:
						rook_index=i
					i+=1
				if rook_index<0:
					return False
				self.y=new_pos[1]
				self.x = new_pos[0]
				pieces[rook_index].x = 5
				pieces[rook_index].y = 7
				return True
			elif new_pos[0]==2 and new_pos[1]==7:
				rook_index = -1
				i=0
				for piece in pieces:
					if piece.y==7 and (piece.x==1 or piece.x==2 or piece.x==3):
						return False
					elif piece.y==7 and piece.x==0 and type(piece)==rook and self.color==piece.color:
						rook_index=i
					i+=1

				if rook_index<0:
					return False
				self.y=new_pos[1]
				self.x = new_pos[0]
				pieces[rook_index].x = 3
				pieces[rook_index].y = 7
				return True
		if (self.x==new_pos[0]+1 or self.x==new_pos[0]-1) and abs(self.y-new_pos[1])<2:
			self.first_move = True
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
		elif self.x==new_pos[0] and abs(self.y-new_pos[1])==1:
			self.first_move = True
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