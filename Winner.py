import pygame

def win(winner):
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    font = pygame.font.Font('freesansbold.ttf', 35)
    text = 'THE WINNER IS:  '+ str(winner).upper()
    text = font.render(text,True,(0,0,0),(255,255,255))
    img = pygame.image.load(r"C:\Users\bassi\OneDrive\Desktop\programmazione\python\pyth\inizipy\tic_tac_toe\win.jpg")
    while True:
        screen.blit(img,(0,0))
        screen.blit(text,(120,240))
    
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
    
                pygame.quit()
    
                quit()
            pygame.display.update()