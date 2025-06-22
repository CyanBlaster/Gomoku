import sys
import pygame
import datetime
import math

def ZeroField(n):
    return [[0] * n for i in range(n)]

def drawX(screen, x, y):
    pygame.draw.line(screen, (0, 255, 0), (x * 25 + 1, y * 25 + 1), (x * 25 + 23, y * 25 + 23))
    pygame.draw.line(screen, (0, 255, 0), (x * 25 + 23, y * 25 + 1), (x * 25 + 1, y * 25 + 23))

def drawO(screen, x, y):
    pygame.draw.circle(screen, (0, 255, 0), (x * 25 + 13, y * 25 + 13), 11)
    pygame.draw.circle(screen, (0, 0, 0), (x * 25 + 13, y * 25 + 13), 10)

def checkRow(board, x, y):
    if(board[x][y] == 0):
        return False
    for i in range(5):
        if(board[x][y] != board[x + i][y]):
            return False
    return True

def checkColumn(board, x, y):
    if(board[x][y] == 0):
        return False
    for i in range(5):
        if(board[x][y] != board[x][y + i]):
            return False
    return True

def checkDiagonalRight(board, x, y):
    if(board[x][y] == 0):
        return False
    for i in range(5):
        if(board[x][y] != board[x + i][y + i]):
            return False
    return True
def checkDiagonalLeft(board, x, y):
    if(board[x][y] == 0):
        return False
    for i in range(5):
        if(board[x][y] != board[x - i][y + i] or x < i or y < i):
            return False
    return True


def checkWin(board):
    for y in range (16):
        for x in range(16):
            if (checkRow(board, x, y)):
                if (board[x][y] == 1):
                    return 1
                elif (board[x][y] == 2):
                    return 2
            elif (checkColumn(board, x, y)):
                if(board[x][y] == 1):
                    return 1
                elif (board[x][y] == 2):
                    return 2
            elif (checkDiagonalRight(board, x, y)):
                if(board[x][y] == 1):
                    return 1
                elif (board[x][y] == 2):
                    return 2
            elif (checkDiagonalLeft(board, x, y)):
                if(board[x][y] == 1):
                    return 1
                elif (board[x][y] == 2):
                    return 2

def main():
    width = 501
    height = 501
    screen = pygame.display.set_mode((width, height))
    running = True
    xIdx = 9
    yIdx = 9
    turn = 1
    board = ZeroField(20)
    while running:
        if(checkWin(board) == 1):
            print("Win X")
            running = False
        elif (checkWin(board) == 2):
            print("Win O")
            running = False
        
        # pygame.draw.line(screen, (255, 0, 0), (zoomX * i + hS, zoomY * f(i) + vS), ((zoomX * (i + 1) + hS, zoomY * f(i + 1) + vS)))
        pygame.display.flip()
        screen.fill((0, 0, 0))
        for i in range(0, 21):
            pygame.draw.line(screen, (0, 0, 255), (i * 500/20, 0), (i * 500/20, 500))
            pygame.draw.line(screen, (0, 0, 255), (0, i * 500/20), (500, i * 500/20))
        pygame.draw.rect(screen, (255, 255, 255), (xIdx * 25 + 1, yIdx * 25 + 1, 24, 24))

        for y in range(20):
            for x in range(20):
                if(board[x][y] == 1):
                    drawX(screen, x, y)
                elif (board[x][y] == 2):
                    drawO(screen, x, y)

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_LEFT:
                    xIdx -= 1
                    if(xIdx == -1):
                        xIdx = 0
                elif events.key == pygame.K_RIGHT:
                    xIdx += 1
                    if(xIdx == 20):
                        xIdx = 19
                elif events.key == pygame.K_UP:
                    yIdx -= 1
                    if(yIdx == -1):
                        yIdx = 0
                elif events.key == pygame.K_DOWN:
                    yIdx += 1
                    if(yIdx == 20):
                        yIdx = 19
                elif events.key == pygame.K_SPACE:
                    if(board[xIdx][yIdx] == 0):
                        if(turn == 1):
                            print(1)
                            board[xIdx][yIdx] = 1
                            turn = 2
                        else:
                            print(2)
                            board[xIdx][yIdx] = 2
                            turn = 1
                    

main()