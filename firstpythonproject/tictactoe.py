from cProfile import label

import pygame
import sys
import numpy as np

pygame.init()
WIDTH = 600
HEIGHT = 600
SQUARE_SIZE = 200
SPACE = 55
CIRCLE_RADIUS = 60
LN_WIDTH = 15
CIRCLE_WIDTH = 15
CROSS_WIDTH = 15
BOARD_ROW = 3
BOARD_COL = 3
BG_COL = (15, 150, 150)
LN_COL = (134, 172, 223)
RED = (255, 0, 0)
CIRCLE_COLOR = (234, 234, 234)
CROSS_COLOR = (55, 55, 55)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COL)

# board
board = np.zeros((BOARD_ROW, BOARD_COL))


def draw_lines():
    pygame.draw.line(screen, LN_COL, (200, 0), (200, 600), LN_WIDTH)  # 1st horizontal line
    pygame.draw.line(screen, LN_COL, (400, 0), (400, 600), LN_WIDTH)  # 2nd horizontal line
    pygame.draw.line(screen, LN_COL, (0, 200), (600, 200), LN_WIDTH)  # 1st vertical line
    pygame.draw.line(screen, LN_COL, (0, 400), (600, 400), LN_WIDTH)  # 2nd vertical line


def draw_figures():
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):

            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (
                    int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * 200 + 55, row * 200 + 200 - 55),
                                 (col * 200 + 200 - 55, row * 200 + 55), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + 55, row * 200 + 55),
                                 (col * 200 + 200 - 55, row * 200 + 200 - 55),
                                 CROSS_WIDTH)

def declare_winner(player):
    import time
    screen.fill(BG_COL)
    font = pygame.font.Font('freesansbold.ttf', 32)
    if winner != 3:
        text = font.render('Player '+str(int(player))+" wins !", False, (0, 0, 0))
    else:
        text = font.render("Draw", False, (0, 0, 0))
    screen.blit(text, (200, 200))
    pygame.display.update()
    time.sleep(1)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def board_fill():
    print(board)
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == 0:
                return 0
    return 1

def get_winner():
    if board_fill() == 1:
        return 3
    # check diagonal
    winner = board[1][1]
    flag = 0
    for i in range(0, 3):
        if board[i][i] != winner:
            flag = 1
    if flag == 0 and winner != 0:
        return winner
    flag = 0
    j = 2
    for i in range(0, 3):
        if board[i][j] != winner:
            flag = 1
        j -= 1
    if flag == 0 and winner != 0:
        return winner
    flag = 0
    # horizontal check
    for i in range(0, 3):
        winner = board[i][0]
        flag = 0
        for j in range(0, 3):
            if board[i][j] != winner:
                flag = 1
        if flag == 0 and winner != 0:
            return winner
    # vertical check
    for i in range(0, 3):
        winner = board[0][i]
        flag = 0
        for j in range(0, 3):
            print(winner, board[j][i])
            if board[j][i] != winner:
                flag = 1
        if flag == 0 and winner != 0:
            return winner
    winner = 0
    return winner


draw_lines()
player = 1

while True:
    for event in pygame.event.get():
        winner = get_winner()
        if event.type == pygame.QUIT or winner != 0:
            declare_winner(winner)
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_X = event.pos[1]
            mouse_Y = event.pos[0]
            clicked_row = int(mouse_X // 200)
            clicked_col = int(mouse_Y // 200)
            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
            if player == 1:
                player = 2
            else:
                player = 1
            draw_figures()
    pygame.display.flip()
