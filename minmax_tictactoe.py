# IMPORTS
import pygame
import time
import math


#VARIABLES
used_spots = []
positions = [[0,0,0],
             [0,0,0],
             [0,0,0]]
players = [0,1]
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

def approximate(val):
    """approxiamate values by defect"""
    if val >=2 or val == 3:
        return 250
    elif val >=1:
        return  150
    elif val >=0:
        return 50 

def draw_X():
    """draws the x, x and y are the centre coordinates"""
    x,y = pygame.mouse.get_pos()
    x = 3*x/300
    y = 3*y/300
    x = approximate(x)
    y = approximate(y)
    pos_x = 0
    pos_y = 0
    if x == 50:pos_x = 0
    elif x == 150:pos_x=1
    elif x == 250:pos_x=2
    if y == 50:pos_y=0
    elif y == 150:pos_y=1
    elif y == 250:pos_y=2
    if positions[pos_y][pos_x] == 0:
        positions[pos_y][pos_x] = -1
        pygame.draw.line(screen,(255,255,255),(x-40,y-40),(x+40,y+40),10)
        pygame.draw.line(screen,(255,255,255),(x+40,y-40),(x-40,y+40),10)
        players.reverse()
    else: 
        print('the spot was occupied')
        time.sleep(.25)

def MinMax(board,player):
    win,winner = is_done(board)
    if win != 'notdone':
        return winner
    if player == 'max':
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j]==0:
                    board[i][j]=1
                    score = MinMax(board, 'min')
                    board[i][j]=0
                    best=max(score,best)
        return best
    if player == 'min':
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j]==0:
                    board[i][j]=-1
                    score = MinMax(board, 'max')
                    board[i][j]=0
                    best=min(score,best)
        return best        



def draw_circle():
    """draws the circle, x and y are the centre coordinates"""
    board = positions.copy()
    best = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                board[i][j]=1
                score = MinMax(board,'min')
                board[i][j]=0
                if score>best:
                    best = score
                    move = [i,j]
    y = move[0]
    x = move[1]
    positions[y][x]=1
    if x == 0: x = 50
    elif x == 1: x = 150
    elif x == 2: x = 250
    if y == 0: y = 50
    elif y == 1: y = 150
    elif y == 2: y = 250
    pygame.draw.circle(screen,(255,255,255),(x,y),-10+WIDTH/6,10)

# GAME FUNCTIONS

def is_done(la):
    """checks if there is a winner"""
    win = 'notdone'
    winner = 0
    if sum(x.count(0) for x in la)==0:win = False
    for i in range(3):
        if la[i][0] == la[i][1] == la[i][2] and la[i][0]!=0:
            win = True
            winner = la[i][0]
        if la[0][i] == la[1][i] == la[2][i] and la[0][i]!=0:
            win = True
            winner = la[0][i]
    if la[0][0] == la[1][1] == la[2][2] and la[0][0]!=0:
        win = True
        winner = la[0][0]    
    elif la[0][2] == la[1][1] == la[2][0] and la[0][2]!=0:
        win = True
        winner = la[i][0]
    return win,winner
       
def new_move():
    """figures out where you want to put the move"""

    if players[0] == 1:
        draw_circle()  
        players.reverse()     
    elif players[0] == 0:
        if  pygame.mouse.get_pressed().count(True)>=1:
                draw_X()   
# UTILS 



running = True
while running:
    """main loop"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        new_move()
        pygame.display.update()
        win,winner = is_done(positions)
        if win==True:
            if winner == 1: winner = 'ai'
            elif winner == -1: winner = 'human'
            pygame.quit()
            from Winner import win
            win(winner)
        elif win == False:
            print('There is no winner')
            quit()
    pygame.display.update()