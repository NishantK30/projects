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
        self.display_text(display_surface,"WELCOME TO THE GAME",450,100)
        self.display_text(display_surface,"Press SPACE to continue",450,400)
        
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.start_game()
            pygame.time.wait(200)

            
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
        self.text_parser = text_parser
        
         
    def create_room(self):
        self.display_surface.fill((94,129,162))
        self.display_bg_image(self.display_surface, room_data[self.current_room]["bg_image_address"])
        self.text_parser(self.display_surface,self.current_room)
        if room_data[self.current_room]['no_of_choices']==1:
            self.display_text(self.display_surface,"press space to continue",450,480 )
        else:
            self.display_text(self.display_surface,room_data[self.current_room]['choice 1'][0],300,430)
            self.display_text(self.display_surface,room_data[self.current_room]['choice 2'][0],300,480)
            
            
        
        
       
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.create_overworld()
        pygame.time.wait(300)
        if room_data[self.current_room]['no_of_choices']==2: 
            if keys[pygame.K_a]:
                self.current_room = room_data[self.current_room]['choice 1'][1]
            if keys[pygame.K_b]:
                self.current_room = room_data[self.current_room]['choice 2'][1]           
        else:
            if keys[pygame.K_SPACE]:
                self.current_room = room_data[self.current_room]['choice 1'][1]
            
          
    
    def run(self):
        self.input()
        self.create_room()
        
    