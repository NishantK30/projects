import pygame
from support import *
from game_data import *

class Overworld:
    def __init__(self,display_surface,start_game) -> None:
        self.display_surface = display_surface
        self.display_text = display_text
        self.display_bg_image = display_bg_image
        self.start_game = start_game
    
    def create_overworld(self, display_surface):
        self.display_bg_image(display_surface, 'images/bg_image.jpg')
        self.display_text(display_surface,450,100,"WELCOME TO THE GAME")
        self.display_text(display_surface,450,400,"Press SPACE to continue")
        
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.start_game()

            
    def run(self):
        self.create_overworld(self.display_surface)
        self.input()
    
        
        
class Room:

    def __init__(self,current_room, create_overworld) -> None:
        super().__init__()
        self.current_room = current_room
        self.display_surface = pygame.display.get_surface()
        self.display_text = display_text
        self.display_bg_image = display_bg_image
        self.create_overworld = create_overworld
        
         
    def create_room(self,current_room):
        self.display_surface.fill((94,129,162))
        self.display_bg_image(self.display_surface, room_data[current_room]["bg_image_address"])
        self.display_text(self.display_surface,450,100,room_data[current_room]["text"])
        self.display_text(self.display_surface,250,400,room_data[current_room]["choice 1"][0])
        self.display_text(self.display_surface,650,400,room_data[current_room]["choice 2"][0])
        
        
       
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.create_overworld()
        if keys[pygame.K_a]:
            self.current_room = room_data[self.current_room]['choice 1'][1]
        if keys[pygame.K_b]:
            self.current_room = room_data[self.current_room]['choice 2'][1]
            
            
    
    def run(self):
        self.input()
        self.create_room(self.current_room)
        
    