import pygame
import sys
from pawn import pawn
from queen import queen
from rook import rook
from knight import knight
from king import king
from bishop import bishop

""" NOTES:
	- I still need to implement en passant
	- I still need to check if king is in check. If he is make sure that player shields or moves king. If that is not possible, then it is a checkmate.
	This is porbably really hard so take time to look into it(or not)
	- Finally implement the server.
"""

# Initialize the game
pygame.init()
clock = pygame.time.Clock()

# Defining some colors
blue = (4, 40, 125)
black = (0, 0, 0)
white = (255,255,255)
back_color = white

# Create screen related variables
rows, cols = 8,8
square = 60
screen_width, screen_height = 200+square*cols, 200+square*rows
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chess")

# The function which draws the chess board
def drawBoard(screen, current_piece, pieces):
	pygame.draw.rect(screen, blue, (99, 99, cols*square+2, cols*square+2), width=1)
	for i in range(rows):
		for j in range(cols):
			if i%2==0:
				if j%2==0:
					pygame.draw.rect(screen, white, (100+j*square, 100+i*square, square, square))
				else:
					pygame.draw.rect(screen, blue, (100+j*square, 100+i*square, square, square))
			else:
				if j%2==0:
					pygame.draw.rect(screen, blue, (100+j*square, 100+i*square, square, square))
				else:
					pygame.draw.rect(screen, white, (100+j*square, 100+i*square, square, square))
	if current_piece or current_piece==0:
		pygame.draw.rect(screen, (0,255,0), (100+pieces[current_piece].x*square, 100+pieces[current_piece].y*square, square, square))

# The function which selects and moves a piece
def selectPiece(pieces, pos, turn):
	i = 0
	for piece in pieces:
		if turn==0 and piece.color=="white":
			if pos[0]==piece.x and pos[1]==piece.y:
				return i
		elif turn==1 and piece.color=="black":
			if pos[0]==piece.x and pos[1]==piece.y:
				return i
		i+=1
	return None

# Making a menu 
def startMenu():
	# Initializing start screen image
	screen_img1 = pygame.image.load("img/startScreen1.png")
	screen_img1 = pygame.transform.scale(screen_img1, (screen_width, int(screen_img1.get_height()*screen_width/screen_img1.get_width())))
	screen_img2 = pygame.image.load("img/startScreen2.png")
	screen_img2 = pygame.transform.scale(screen_img2, (screen_width, int(screen_img2.get_height()*screen_width/screen_img2.get_width())))

	# Setting up the start button
	font = pygame.font.Font('freesansbold.ttf', 40)
	text = font.render("Start !", True, black)
	font = pygame.font.Font('freesansbold.ttf', 20)
	exit_text = font.render("Exit", True, black)
	
	# Creating the hover boolean
	hover = False

	while True:

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONUP:
				if pygame.mouse.get_pos()[0]>240 and pygame.mouse.get_pos()[0]<440 and pygame.mouse.get_pos()[1]>303 and pygame.mouse.get_pos()[1]<378:
					main()
				if pygame.mouse.get_pos()[0]>315 and pygame.mouse.get_pos()[0]<365 and pygame.mouse.get_pos()[1]>645 and pygame.mouse.get_pos()[1]<675:
					pygame.quit()
					quit()
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		# Setting back the screen back to background color
		screen.fill(white)

		# Showing the start screen image
		screen.blit(screen_img1, (0, 150))
		screen.blit(screen_img2, (0, 425))

		# Creating a Start Button
		if pygame.mouse.get_pos()[0]>240 and pygame.mouse.get_pos()[0]<440 and pygame.mouse.get_pos()[1]>303 and pygame.mouse.get_pos()[1]<378:
			pygame.draw.rect(screen, (200,200,200), (240, 303, 200, 75))
		else:
			pygame.draw.rect(screen, (150,150,150), (240, 303, 200, 75))
		pygame.draw.rect(screen, black, (240, 303, 200, 75), width=2)
		screen.blit(text, (281, 321))

		# Creating the exit button
		if pygame.mouse.get_pos()[0]>315 and pygame.mouse.get_pos()[0]<365 and pygame.mouse.get_pos()[1]>645 and pygame.mouse.get_pos()[1]<675:
			pygame.draw.rect(screen, (200,200,200), (315, 645, 50, 30))
		else:
			pygame.draw.rect(screen, (150,150,150), (315, 645, 50, 30))
		pygame.draw.rect(screen, black, (315, 645, 50, 30), width=2)
		screen.blit(exit_text, (321, 650))

		pygame.display.update()
		clock.tick(15)

# This function will check for a winner, which is when a king is killed
def checkForWinner(pieces):
	black_king = False
	white_king = False

	for piece in pieces:
		if type(piece)==king:
			if piece.color=="black":
				black_king=True
			elif piece.color=="white":
				white_king=True

	if not black_king:
		return "white"
	elif not white_king:
		return "black"
	else:
		return None

# Making a gameover screen
def gameOver(winner):
	# Initializing start screen image
	if winner=="black":
		screen_img = pygame.image.load("img/startScreen1.png")
		screen_img = pygame.transform.scale(screen_img, (screen_width, int(screen_img.get_height()*screen_width/screen_img.get_width())))
	else:
		screen_img = pygame.image.load("img/startScreen2.png")
		screen_img = pygame.transform.scale(screen_img, (screen_width, int(screen_img.get_height()*screen_width/screen_img.get_width())))

	# Setting up the start button
	font = pygame.font.Font('freesansbold.ttf', 40)
	button_text = font.render("Play Again !", True, black)
	font = pygame.font.Font('freesansbold.ttf', 20)
	exit_text = font.render("Exit", True, black)
	font = pygame.font.SysFont("comicsansms", 61)
	if winner=="white":
		winner_text = font.render("White won !", True, black)
	else:
		winner_text = font.render("Black won !", True, black)
	
	# Creating the hover boolean
	hover = False

	while True:

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONUP:
				if pygame.mouse.get_pos()[0]>215 and pygame.mouse.get_pos()[0]<465 and pygame.mouse.get_pos()[1]>303 and pygame.mouse.get_pos()[1]<378:
					main()
				if pygame.mouse.get_pos()[0]>315 and pygame.mouse.get_pos()[0]<365 and pygame.mouse.get_pos()[1]>645 and pygame.mouse.get_pos()[1]<675:
					pygame.quit()
					quit()
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		# Setting back the screen back to background color
		screen.fill(white)

		# Showing the screen image
		screen.blit(screen_img, (0, 425))
		screen.blit(winner_text, (170, 150))

		# Creating a play again Button
		if pygame.mouse.get_pos()[0]>215 and pygame.mouse.get_pos()[0]<465 and pygame.mouse.get_pos()[1]>303 and pygame.mouse.get_pos()[1]<378:
			pygame.draw.rect(screen, (200,200,200), (215, 303, 250, 75))
		else:
			pygame.draw.rect(screen, (150,150,150), (215, 303, 250, 75))
		pygame.draw.rect(screen, black, (215, 303, 250, 75), width=2)
		screen.blit(button_text, (224, 321))

		# Creating the exit button
		if pygame.mouse.get_pos()[0]>315 and pygame.mouse.get_pos()[0]<365 and pygame.mouse.get_pos()[1]>645 and pygame.mouse.get_pos()[1]<675:
			pygame.draw.rect(screen, (200,200,200), (315, 645, 50, 30))
		else:
			pygame.draw.rect(screen, (150,150,150), (315, 645, 50, 30))
		pygame.draw.rect(screen, black, (315, 645, 50, 30), width=2)
		screen.blit(exit_text, (321, 650))

		pygame.display.update()
		clock.tick(15)

# Game loop
def main():
	# Creating all pieces and putting them into one list
	pieces  = [pawn(i, 1, "black", square) for i in range(8)]
	pieces += [rook(0, 0, "black", square), rook(7, 0, "black", square), queen(3, 0, "black", square), knight(1, 0, "black", square), knight(6, 0, "black", square), bishop(2, 0, "black", square), bishop(5, 0, "black", square), king(4, 0, "black", square)]
	pieces += [pawn(i, 6, "white", square) for i in range(8)]
	pieces += [rook(0, 7, "white", square), rook(7, 7, "white", square), queen(3, 7, "white", square), knight(1, 7, "white", square), knight(6, 7, "white", square), bishop(2, 7, "white", square), bishop(5, 7, "white", square), king(4, 7, "white", square)]

	# Setting up initial variables
	turn = 0 
	current_piece = None
	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONUP:
				x, y = pygame.mouse.get_pos()
				x-=100
				y-=100
				x=int(x/square)
				y=int(y/square)
				pos = (x, y)
				if current_piece or current_piece==0:
					s=0
					if pieces[current_piece].color=="white":
						s=-1
					done = pieces[current_piece].move(pieces, pos)
					current_piece+=s
					if done:
						if type(pieces[current_piece])==pawn:
							if pieces[current_piece].checkForUpgrade():
								pieces[current_piece] = queen(pieces[current_piece].x, pieces[current_piece].y, pieces[current_piece].color, square)
						turn +=1
						turn%=2
						# Check for a winner
						if checkForWinner(pieces):
							gameOver(checkForWinner(pieces))

					current_piece = None
				else:
					current_piece = selectPiece(pieces, pos, turn)
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		# Setting back the screen back to background color
		screen.fill(back_color)

		# Drawing on the screen
		drawBoard(screen, current_piece, pieces)
		
		# Drawing all the pieces
		for piece in pieces:
			piece.draw(screen)

		clock.tick(15)
		pygame.display.update()

# Starting the function
startMenu()
