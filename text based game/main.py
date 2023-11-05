import pygame,sys
from Room import Room,Overworld


class Game:
    def __init__(self) -> None:
        self.overworld = Overworld(screen,self.start_game)
        self.status = 'overworld'
        self.current_room = 0
    
    def start_game(self):
        self.room = Room(self.current_room, self.create_overworld)
        self.status = "game_running" 
        
    def create_overworld(self):
        self.overworld = Overworld(screen,self.start_game)
        self.status = 'overworld'
        
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
            
    game.run()
    pygame.display.update()
    