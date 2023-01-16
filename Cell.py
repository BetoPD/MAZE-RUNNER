import pygame
import random
import time
RES = WIDTH, HEIGHT = 800, 800
TILE = 40
cols, rows = HEIGHT // TILE, WIDTH // TILE 
pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wall = {"top": True, "right": True, "bottom": True, "left": True}
        self.visited = False
    
    def show(self):
        x = self.x * TILE
        y = self.y * TILE

        if self.visited:
            pygame.draw.rect(sc, pygame.Color("red"), (x, y, TILE, TILE))
        if self.wall["top"]:
            pygame.draw.line(sc, pygame.Color("yellow"), (x, y), (x + TILE, y), 2)
        if self.wall["right"]:
            pygame.draw.line(sc, pygame.Color("yellow"), (x + TILE, y), (x + TILE, y + TILE), 2)
        if self.wall["bottom"]:
            pygame.draw.line(sc, pygame.Color("yellow"), (x + TILE, y + TILE), (x, y + TILE), 2)
        if self.wall["left"]:
            pygame.draw.line(sc, pygame.Color("yellow"), (x, y + TILE), (x, y), 2)
    
    def index(self, x, y):
        if ( x < 0 or y < 0 or x > (cols - 1) or y > (rows - 1)):
            return False
        return x + y  * cols

    def check_neighbors(self):
        neighbors = []
        x = current.x
        y = current.y
        top = grid[self.index(x, y - 1)]
        right = grid[self.index(x + 1, y)]
        bottom = grid[self.index(x, y + 1)]
        left = grid[self.index(x  - 1, y)]

        if (top and not top.visited):
            neighbors.append(top)
        if (right and not right.visited):
            neighbors.append(right)
        if (bottom and not bottom.visited):
            neighbors.append(bottom)
        if (left and not left.visited):
            neighbors.append(left)
        
        if(len(neighbors) > 0):
            random_value = random.randrange(0, len(neighbors))
            return neighbors[random_value]
        else:
            return False

def remove_Walls(current, next):
    x = current.x - next.x
    if x == 1:
        current.wall["left"] = False
        next.wall["right"] = False
    elif x == -1:
        current.wall["right"] = False
        next.wall["left"] = False
    y = current.y - next.y
    if y == 1:
        current.wall["top"] = False
        next.wall["bottom"] = False
    elif y == -1:
        current.wall["bottom"] = False
        next.wall["top"] = False

        
        
grid = [Cell(col, row) for row in range(rows) for col in range(cols)]
current = grid[0]
current.visited = True
stack = []
path = []
stack.append(current)     
while True:
    sc.fill(pygame.Color("black"))
    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            exit()
    for cell in grid:
        cell.show()
    
    if len(stack) > 0:
        next = current.check_neighbors()
        if next:
            next.visited = True
            remove_Walls(current,next)
            current = next
            stack.append(current)
        else:
            current = stack.pop()
        


    pygame.display.flip()
    clock.tick(1)
