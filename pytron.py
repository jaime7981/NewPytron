import sys, pygame
from pygame.locals import *
from map import *
from players import *

length = 30
dim = length**2

mainmap = Map(length)

default_player_keys = [K_w, K_s, K_a, K_d]
players = []

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

def AddPlayer():
    newplayer = Player("Random Player", GRAY, default_player_keys, length-1)
    if mainmap.PlacePlayer(surface, newplayer) == True:
        players.append(newplayer)
        for player in players:
            print(player.name)
        print(len(players))

def game_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_p:
                AddPlayer()

def main():
    mainmap.DrawMap(surface)

    playerone = Player("Jamie", RED, default_player_keys, length-1)
    mainmap.PlacePlayer(surface, playerone)
    players.append(playerone)

    playerotwo = Player("Jamie", GREEN, default_player_keys, length-1)
    mainmap.PlacePlayer(surface, playerotwo)
    players.append(playerotwo)

    while True:
        game_events()
        pygame.display.update()
        clock.tick(240)

if __name__ == "__main__":    
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((dim+1,dim+1))
    surface.fill((0,0,0))
    main()
