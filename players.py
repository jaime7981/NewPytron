
import random
import pygame
from pygame.locals import *

playercount = 0

class Player():
    def __init__(self, name, color, player_keys, mapdimention, id, AI):
        self.name = name
        self.playerid = id
        self.AI = AI
        self.position = [random.randint(0,mapdimention), random.randint(0,mapdimention)]
        self.color = color
        self.key_dict = {player_keys[0]:"up", player_keys[1]:"down", player_keys[2]:"left", player_keys[3]:"right"}
        self.orientation = {"up": 1, "down": 0, "left": 0, "right": 0} #It could be changed to up-down 1/-1 and left-right 1/-1

    #This handles the key inputs and prevents the player for moving backwards
    def PlayerOrientation(self, orientation):
        if orientation == "up" and self.orientation["down"] == 1:
            return False
        elif orientation == "down" and self.orientation["up"] == 1:
            return False
        elif orientation == "left" and self.orientation["right"] == 1:
            return False
        elif orientation == "right" and self.orientation["left"] == 1:
            return False

        for orient in self.orientation:
            self.orientation[orient] = 0
        self.orientation[orientation] = 1
        return True


        
