import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 500 #Window Height
WINDOW_WIDTH = 500 #Window Width



def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    #Make list with black squares. You may need change this list when you change size of grid.
    lst = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                lst[mouse[1]//25][mouse[0]//25] = 1
                snake((mouse[0]//25)*25,(mouse[1]//25)*25)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    SCREEN.fill(BLACK)
                    drawGrid()
                    lst = move(lst)
                    for i in range(20):
                        for j in range(20):
                            if lst[i][j] == 1:
                                snake(j * 25, i * 25)

        pygame.display.update()

def drawGrid():
    blockSize = 25 #Set the size of the grid block
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def snake(x, y):
    blocksize = 25
    head_rect = pygame.Rect(x, y, blocksize, blocksize)
    pygame.draw.rect(SCREEN, WHITE, head_rect)

def alive_or_dead(lst,i,j):
    sum = 0
    if i >= 1 and j >= 1 and lst[i-1][j-1] == 1:
        sum += 1
    if j >= 1 and lst[i][j-1] == 1:
        sum += 1
    if i <= 18 and j >= 1 and lst[i+1][j-1] == 1:
        sum += 1
    if i >= 1 and lst[i-1][j] == 1:
        sum += 1
    if i >= 1 and j <= 18 and lst[i-1][j+1] == 1:
        sum += 1
    if j <= 18 and lst[i][j+1] == 1:
        sum += 1
    if i <= 18 and lst[i+1][j] == 1:
        sum += 1
    if i <= 18 and j <= 18 and lst[i+1][j+1] == 1:
        sum += 1
    if sum == 0 or sum == 1 or sum == 4 or sum == 5 or sum == 6 or sum == 7 or sum == 8:
        return 0
    elif sum == 3:
        return 1
    elif sum == 2 and lst[i][j] == 1:
        return 1


def move(lst):
    lst2 = []
    for i in range(20):
        lst1 = []
        for j in range(20):
            lst1.append(alive_or_dead(lst,i,j))
        lst2.append(lst1)
    return lst2

main()