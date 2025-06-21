import sys
import pygame
import datetime
import math

def ZeroField(n):
    return [[0] * n for i in range(n)]

def drawX(screen, x, y):
    pygame.draw.line(screen, (0, 255, 0), (x * 25, y * 25), (x * 25 + 24, y * 25 + 24))
    pygame.draw.line(screen, (0, 255, 0), (x * 25 + 24, y * 25), (x * 25, y * 25 + 24))

def drawO(screen, x, y):
    pygame.draw.circle(screen, (0, 255, 0), (x * 25 + 13, y * 25 + 13), 12)
    pygame.draw.circle(screen, (0, 0, 0), (x * 25 + 13, y * 25 + 13), 11)

def main():
    width = 501
    height = 501
    screen = pygame.display.set_mode((width, height))
    running = True
    xIdx = 0
    yIdx = 0
    board = ZeroField(20)
    while running:

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
                        print(1)
                        board[xIdx][yIdx] = 1
                    

main()