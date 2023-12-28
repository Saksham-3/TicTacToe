import pygame, sys
import numpy as np



pygame.init()

WIDTH = 600
HEIGHT = 600
GREY = (23, 145, 135 )
BACKGROUND = (100, 207, 204)
LINE_W = 15
BOARD_R = 3
BOARD_C = 3
RADIUS = 60
CIRCLE_WIDTH = 15
CIRCLE_color = (239, 231, 200)
X_color = (66,66,66)
X_WIDTH = 25
X_SPACE = 55


screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
pygame.display.set_caption('Tic-Tac-Toe')
screen.fill(BACKGROUND)

board = np.zeros((BOARD_R, BOARD_C))
#print(board)

def create_lines():
    pygame.draw.line(screen, GREY, (0,200), (600,200), LINE_W)
    pygame.draw.line(screen, GREY, (0,400), (600,400), LINE_W)
    pygame.draw.line(screen, GREY, (200,0), (200,600), LINE_W)
    pygame.draw.line(screen, GREY, (400,0), (400,600), LINE_W)

def draw_shape():
    for row in range(BOARD_R):
        for col in range(BOARD_C):
            if board[row][col] == 1:
                pygame.draw.circle( screen, CIRCLE_color, (int(col*200 + 100), int(row * 200 + 100 )), RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, X_color, (col * 200 + X_SPACE, row * 200 + 200 - X_SPACE), (col * 200 + 200 - X_SPACE, row * 200 + X_SPACE), X_WIDTH)
                pygame.draw.line(screen, X_color, (col * 200 + X_SPACE, row * 200 + X_SPACE), (col * 200 + 200 - X_SPACE, row * 200 + 200 - X_SPACE), X_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player

def free_square(row,col):
    return board[row][col] == 0
    
def board_full():
    for row in range(BOARD_R):
        for col in range(BOARD_C):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    for col in range(BOARD_C):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_w(col, player)
            return True
        
    for row in range(BOARD_R):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_w(row, player)
            return True
        
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc(player)
        return True
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc(player)
        return True
    
    return False

def draw_vertical_w(col,player):
    posX = col * 200 + 100
    if player == 1:
        color = CIRCLE_color
    elif player == 2:
       color = X_color

    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT-15), 15)

def draw_horizontal_w(row, player):
    posY = row * 200 + 100
    if player == 1:
        color = CIRCLE_color
    elif player == 2:
       color = X_color
    pygame.draw.line(screen, color, (15,posY), (WIDTH - 15, posY), 15)

def draw_asc(player):
    if player == 1:
        color = CIRCLE_color
    elif player == 2:
       color = X_color
    pygame.draw.line(screen,color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)
    
def draw_desc(player):
    if player == 1:
        color = CIRCLE_color
    elif player == 2:
       color = X_color
    pygame.draw.line(screen, color, (15,15), (WIDTH-15, HEIGHT - 15), 15)

def restart():
    screen.fill(BACKGROUND)
    create_lines()
    player = 1
    for row in range(BOARD_R):
        for col in range(BOARD_C):
            board[row][col] = 0

create_lines()

player = 1
gg = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not gg:
            mouseX= event.pos[0]
            mouseY = event.pos[1]
            row_click = int(mouseY // 200)
            col_click = int(mouseX // 200)

            if free_square( row_click, col_click):
                mark_square(row_click, col_click, player)
                if check_win(player):
                    gg = True
                player = player % 2 + 1
                
                draw_shape()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                gg = False

    pygame.display.update()

