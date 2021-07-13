# IMPORTS
import pygame
import time

#VARIABLES
used_spots = []
positions = [[0,0,0],[0,0,0],[0,0,0]]
turn = 0
WIDTH = 300
HEIGHT = 300

# PYGAME SETUP
pygame.init()
screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption('TIC TAC TOE')

# DRAW FUNCTIONS
def draw_grid():
    """draws the grid on the screen"""
    screen.fill((0,0,0))
    pygame.draw.line(screen, (255,255,255),(WIDTH/3,0),(WIDTH/3,HEIGHT))
    pygame.draw.line(screen, (255,255,255),(2*WIDTH/3,0),(2*WIDTH/3,HEIGHT))
    pygame.draw.line(screen, (255,255,255),(0,HEIGHT/3),(WIDTH,HEIGHT/3))
    pygame.draw.line(screen, (255,255,255),(0,2*HEIGHT/3),(WIDTH,2*HEIGHT/3))
draw_grid()

def draw_X(x,y):
    """draws the x, x and y are the centre coordinates"""
    pygame.draw.line(screen,(255,255,255),(x-40,y-40),(x+40,y+40),10)
    pygame.draw.line(screen,(255,255,255),(x+40,y-40),(x-40,y+40),10)


def draw_circle(x,y):
    """draws the circle, x and y are the centre coordinates"""
    pygame.draw.circle(screen,(255,255,255),(x,y),-10+WIDTH/6,10)

# GAME FUNCTIONS
def draw_move(turn,x,y):
    """creates a list with all of the positions that need to be drawn eanch frame,
    and puts who moved in the list positions"""
    if x == 50:pos_x = 0
    elif x == 150:pos_x=1
    elif x == 250:pos_x=2
    if y == 50:pos_y=0
    elif y == 150:pos_y=1
    elif y == 250:pos_y=2

    used_spots.append([x,y])
    if turn == 0:
        draw_circle(x,y)
        positions[pos_y][pos_x] = 1
        
    elif turn == 1:
        draw_X(x,y)
        positions[pos_y][pos_x] = 2

def is_done():
    """checks if there is a winner"""
    win = False
    winner = 0
    for i in range(3):
        if positions[i][0] == positions[i][1] == positions[i][2] and positions[i][0]!=0:
            win = True
            winner = positions[i][0]
        if positions[0][i] == positions[1][i] == positions[2][i] and positions[0][i]!=0:
            win = True
            print(positions[0][i])
            winner = positions[0][i]
    if positions[0][0] == positions[1][1] == positions[2][2] and positions[0][0]!=0:
        win = True
        winner = positions[0][0]    
    elif positions[0][2] == positions[1][1] == positions[2][0] and positions[0][2]!=0:
        win = True
        winner = positions[i][0]
    if winner == 1: winner = "circle"
    elif winner == 2: winner = "X"
    if win == True:
        print(str(winner) + '\twon')
        time.sleep(2)
        pygame.quit()
        quit()
    elif win == False and sum(x.count(0) for x in positions)==0:
        print('there is no winner')
        time.sleep(2)
        pygame.quit()
        quit()
       
def new_move():
    """figures out where you want to put the move"""
    global turn
    x,y = pygame.mouse.get_pos()
    x = 3*x/300
    y = 3*y/300
    grid_x = approximate(x)
    grid_y = approximate(y)
    if used_spots.count([grid_x,grid_y]) == 0:
        turn+=1
        draw_move(turn%2,grid_x,grid_y)
    else: print('please use only available spots')

# UTILS 
def approximate(val):
    """approxiamate values by defect"""
    if val >=2 or val == 3:
        return 250
    elif val >=1:
        return  150
    elif val >=0:
        return 50 


running = True
while running:
    """main loop"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif  pygame.mouse.get_pressed().count(True)>=1:
            new_move()
            pygame.display.update()
            is_done()
    pygame.display.update()