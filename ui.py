import pygame
from button import Button

pygame.init()

screen = pygame.display.set_mode((500, 500))

screen.fill((0,0,0))

font = pygame.font.Font('freesansbold.ttf', 30)

text = font.render('do you want to play tic tac toe', True, (255,255,255), (0,0,0))
button1 = Button(50,300,'against my ai?',(255,255,255),(0,0,0))
button2 = Button(250,300,'against a friend?',(255,255,255),(0,0,0))
button1.display()
button2.display()


textrect = text.get_rect()

textrect.center = (250, 100)

while True:
    button1.render(screen)
    button2.render(screen)
    screen.blit(text,textrect)
 
    for event in pygame.event.get():
 
        if event.type == pygame.QUIT:
 
            pygame.quit()
 
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:

            if button1.is_clicked():
                pygame.quit()
                import minmax_tictactoe
            elif button2.is_clicked():
                pygame.quit()
                import tic_tac_toe 
        pygame.display.update()
    #button1.hover(screen)
    