import sys, pygame
from pygame.locals import *
from map import *
from players import *

length = 30
dim = length**2

mainmap = Map(length)

default_player_one_keys = [K_w, K_s, K_a, K_d]
default_player_two_keys = [K_UP, K_DOWN, K_LEFT, K_RIGHT]
default_player_extra_keys = [K_i, K_k, K_j, K_l]

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

def game_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            for player in mainmap.players:
                if event.key in player.key_dict:
                    player.PlayerOrientation(player.key_dict[event.key])
                    print(player.name, player.key_dict[event.key], player.orientation)
            if event.key == K_p:
                newplayer = Player("Random Player", GRAY, default_player_extra_keys, length-1)
                mainmap.PlacePlayer(surface, newplayer)
            elif event.key == K_c:
                mainmap.ClearMap(surface)

def main():
    mainmap.DrawMap(surface)

    playerone = Player("Jamie", RED, default_player_one_keys, length-1)
    mainmap.PlacePlayer(surface, playerone)

    playerotwo = Player("Manuel", GREEN, default_player_two_keys, length-1)
    mainmap.PlacePlayer(surface, playerotwo)

    while True:
        game_events()
        mainmap.MovePlayers(surface)
        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":    
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((dim+1,dim+1))
    surface.fill((0,0,0))
    main()
