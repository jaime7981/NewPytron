import pygame
from players import *

#1.- Make squares
#2.- Spawn players
#3.- Move players
#4.- Set bundaries

class Map():
    def __init__(self, dimention):
        self.dimention = dimention
        self.mappositions = []
        self.players = []

    def DrawMap(self,surface):
        for xcord in range(self.dimention):
            aux = []
            for ycord in range(self.dimention):
                x = xcord*self.dimention
                y = ycord*self.dimention
                pygame.draw.rect(surface, (225,225,225), (x, y, self.dimention, self.dimention), 2)
                aux.append(0)
            self.mappositions.append(aux)

    def ClearMap(self, surface):
        self.mappositions = []
        surface.fill((0,0,0))
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
            self.players.append(player)
        else:
            return False

        x = player.position[0]*self.dimention
        y = player.position[1]*self.dimention
        pygame.draw.rect(surface, player.color, (x, y, self.dimention, self.dimention))
        return True

    def MovePlayers(self, surface):
        for player in self.players:
            #Get orientation
            for orientation in player.orientation:
                if player.orientation[orientation] == 1:
                    orient = orientation
                    print(orient)
                    print(player.position)
            
            #Move the player between the walls
            if orient == "left":
                if player.position[0] - 1 >= 0 and self.mappositions[player.position[0] - 1][player.position[1]] != 1:
                    self.mappositions[player.position[0] - 1][player.position[1]] = 1
                    player.position[0] -= 1
                    x = player.position[0]*self.dimention
                    y = player.position[1]*self.dimention
                    pygame.draw.rect(surface, player.color, (x, y, self.dimention, self.dimention))
                else:
                    print(player.name + " Loose")
                    self.players.remove(player)
                    
            elif orient == "right":
                if player.position[0] + 1 < self.dimention and self.mappositions[player.position[0] + 1][player.position[1]] != 1:
                    self.mappositions[player.position[0] + 1][player.position[1]] = 1
                    player.position[0] += 1
                    x = player.position[0]*self.dimention
                    y = player.position[1]*self.dimention
                    pygame.draw.rect(surface, player.color, (x, y, self.dimention, self.dimention))
                else:
                    print(player.name + " Loose")
                    self.players.remove(player)

            elif orient == "up":
                if player.position[1] - 1 >= 0 and self.mappositions[player.position[0]][player.position[1] - 1] != 1:
                    self.mappositions[player.position[0]][player.position[1] - 1] = 1
                    player.position[1] -= 1
                    x = player.position[0]*self.dimention
                    y = player.position[1]*self.dimention
                    pygame.draw.rect(surface, player.color, (x, y, self.dimention, self.dimention))
                else:
                    print(player.name + " Loose")
                    self.players.remove(player)

            elif orient == "down":
                if player.position[1] + 1 < self.dimention and self.mappositions[player.position[0]][player.position[1] + 1] != 1:
                    self.mappositions[player.position[0]][player.position[1] + 1] = 1
                    player.position[1] += 1
                    x = player.position[0]*self.dimention
                    y = player.position[1]*self.dimention
                    pygame.draw.rect(surface, player.color, (x, y, self.dimention, self.dimention))
                else:
                    print(player.name + " Loose")
                    self.players.remove(player)
