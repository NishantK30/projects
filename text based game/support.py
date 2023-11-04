import pygame

def render_text(text, font_size, font_color=(255,255,255)):
       font = pygame.font.Font(None,font_size)
       text_surface = font.render(text,True,font_color) 
       return text_surface, text_surface.get_rect()
   
def display_text(display_surface,width, height, text, font_size = 48):
    welcome_text , welcome_rect = render_text(text,font_size)
    welcome_rect.center = (width,height)
    display_surface.blit(welcome_text,welcome_rect)
    
def display_bg_image(display_surface,img_address):
        bg_imag = pygame.image.load(img_address)
        display_surface.blit(bg_imag,(0,0))
    
