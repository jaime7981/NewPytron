import pygame
from players import *

#1.- Make squares
#2.- Set bundaries
#3.- Spawn players
#4.- Move players

class Map():
    def __init__(self, dimention):
        self.dimention = dimention
        self.mappositions = []


    def DrawMap(self,surface):
        for xcord in range(self.dimention):
            aux = []
            for ycord in range(self.dimention):
                x = xcord*self.dimention
                y = ycord*self.dimention
                pygame.draw.rect(surface, (225,225,225), (x, y, self.dimention, self.dimention), 2)
                aux.append(0)
            self.mappositions.append(aux)

    def PlacePlayer(self, surface, player):
        for pos in player.position:
            if pos >= self.dimention or pos < 0:
                return False
        
        if self.mappositions[player.position[0]][player.position[1]] == 0:
            self.mappositions[player.position[0]][player.position[1]] = 1
        else:
            return False

        x = player.position[0]*self.dimention
        y = player.position[1]*self.dimention
        pygame.draw.rect(surface, player.color, (x, y, self.dimention, self.dimention))
        return True