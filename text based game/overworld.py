import pygame

class Overworld:
    def __init__(self) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        
    def render_text(self,text, font_size, font_color=(255,255,255)):
       font = pygame.font.Font(None,font_size)
       text_surface = font.render(text,True,font_color) 
       return text_surface, text_surface.get_rect()
   
    def display_text(self):
        welcome_text , welcome_rect = self.render_text('WELCOME',48)
        welcome_rect.center = (300,200)
        self.display_surface.blit(welcome_text,welcome_rect)
    
    def display_bg_image(self):
        bg_imag = pygame.image.load('text based game/images/bg_image.jpg')
        self.display_surface.blit(bg_imag,(0,0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.display_surface.fill((94,129,162))
                
    def run(self):
        self.display_text()
        self.display_bg_image()