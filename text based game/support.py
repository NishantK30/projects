import pygame
from game_data import room_data

def render_text(text, font_size, font_color):
       font = pygame.font.Font(None,font_size)
       text_surface = font.render(text,True,font_color) 
       return text_surface, text_surface.get_rect()
   
def display_text(display_surface,text = ' ', width = 450,height=100, font_size = 48,font_color =(255,255,255)):
    welcome_text , welcome_rect = render_text(text,font_size,font_color)
    welcome_rect.center = (width,height)
    display_surface.blit(welcome_text,welcome_rect)

 
def text_parser(display_surface,current_room):
   height = 50
   for line in room_data[current_room]['text']:
        display_text(display_surface,line,height=height, font_size=40,font_color=room_data[current_room]['font_colour'])
        height += 30 


 
def display_bg_image(display_surface,img_address):
        bg_imag = pygame.image.load(img_address)
        display_surface.blit(bg_imag,(0,0))
    

