
import random
import pygame
from pygame.locals import *

#1.- The player have to move
#2.- The player have to change direction
#3.- The player have to draw his line
#4.- Colisions are needed

class Player():
    def __init__(self, name, color, player_keys, mapdimention):
        self.name = name
        self.position = [random.randint(0,mapdimention), random.randint(0,mapdimention)]
        self.line = []
        self.color = color
        self.key_dict = {player_keys[0]:"up", player_keys[1]:"down", player_keys[2]:"left", player_keys[3]:"right"}

    def PressedKey(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in self.key_dict:
                    move = self.key_dict[event.key]
                    print(move)

        
