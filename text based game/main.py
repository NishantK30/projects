import pygame,sys
from overworld import Overworld
from Room import Room


class Game:
    def __init__(self) -> None:
        self.overworld = Overworld()
        self.status = 'overworld'
        
    def create_level(self,current_room):
        self.room = Room(current_room)
        
    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        else:
            self.room.run()

pygame.init()
screen = pygame.display.set_mode((900,506))
pygame.display.set_caption('Text Based Game')
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill((94,129,162))
    game.run()
    pygame.display.update()
    
    