import pygame

class Button:
    def __init__(self, x, y, text,textColor, bgcolor):
        self.x = x
        self.y = y
        self.text = text
        self.bgcolor = bgcolor
        self.textColor = textColor
        self.font = pygame.font.Font('freesansbold.ttf', 20)
    def display(self):
        self.btext = self.font.render(self.text,True,self.textColor,self.bgcolor)
        self.size = self.btext.get_size()
        self.textRect = pygame.Rect(self.x,self.y,self.size[0],self.size[1])

    def render(self,screen):
        screen.blit(self.btext,self.textRect)

    def is_clicked(self):
        mouseX,mouseY = pygame.mouse.get_pos()
        if self.x<mouseX<(self.x+self.size[0]) and self.y < mouseY < (self.y+self.size[1]):
            return True
    
"""     def hover(self,screen):
        mouseX,mouseY = pygame.mouse.get_pos()
        if self.x<mouseX<(self.x+self.size[0]) and self.y < mouseY < (self.y+self.size[1]):
            pygame.draw.rect(screen,(125,125,125),[self.x,self.y,self.size[0],self.size[1]]) """  