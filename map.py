import pygame
from players import *

class Map():
    def __init__(self, dimention):
        self.dimention = dimention
        self.mappositions = []
        self.players = []
        self.playercount = 1

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

    def PlayerDistanceLine(self):
        counterlist = {"up": 0, "down": 0, "left": 0, "right": 0}
        for player in self.players:
            x = player.position[0]
            y = player.position[1]

            for xcord in range(x + 1, len(self.mappositions)):
                if self.mappositions[xcord][y] == 1 and player.orientation["left"] != 1:
                    counterlist["right"] = xcord - x
                    break
                else:
                    counterlist["right"] = len(self.mappositions) - x
            
            for xcord in range(x-1, 0, -1):
                if self.mappositions[xcord][y] == 1 and player.orientation["right"] != 1:
                    counterlist["left"] = x - xcord
                    break
                else:
                    counterlist["left"] = x

            for ycord in range(y + 1, len(self.mappositions)):
                if self.mappositions[x][ycord] == 1 and player.orientation["up"] != 1:
                    counterlist["down"] = ycord - y
                    break
                else:
                    counterlist["down"] = len(self.mappositions) - y

            for ycord in range(y-1, 0, -1):
                if self.mappositions[x][ycord] == 1 and player.orientation["down"] != 1:
                    counterlist["up"] = y - ycord
                    break
                else:
                    counterlist["up"] = y
                        
        print(counterlist)

    def PlacePlayer(self, surface, player):
        for pos in player.position:
            if pos >= self.dimention or pos < 0:
                return False
        
        if self.mappositions[player.position[0]][player.position[1]] == 0:
            if player.playerid != 1:
                self.playercount += 1
            player.playerid = self.playercount
            self.mappositions[player.position[0]][player.position[1]] = player.playerid
            self.players.append(player)
        else:
            return False

        x = player.position[0]*self.dimention
        y = player.position[1]*self.dimention
        pygame.draw.rect(surface, player.color, (x, y, self.dimention, self.dimention))
        print(player.playerid)
        return True

    def MovePlayers(self, surface):
        for player in self.players:
            #Get orientation
            for orientation in player.orientation:
                if player.orientation[orientation] == 1:
                    orient = orientation
            
            #Move the player between the walls
            if orient == "left":
                if player.position[0] - 1 >= 0:
                    if self.mappositions[player.position[0] - 1][player.position[1]] == 0:
                        self.MoveLeft(surface, player)
                    elif player.AI == True and self.mappositions[player.position[0] - 1][player.position[1]] != 1 and self.mappositions[player.position[0] - 1][player.position[1]] != player.playerid:
                        self.MoveLeft(surface, player)
                    else:
                        print(player.name + " Loose by crash")
                        self.players.remove(player)
                else:
                    print(player.name + " Loose by falling off")
                    self.players.remove(player)
                    
            elif orient == "right":
                if player.position[0] + 1 < self.dimention:
                    if self.mappositions[player.position[0] + 1][player.position[1]] == 0:
                        self.MoveRight(surface, player)
                    elif player.AI == True and self.mappositions[player.position[0] + 1][player.position[1]] != 1 and self.mappositions[player.position[0] + 1][player.position[1]] != player.playerid:
                        self.MoveRight(surface, player)
                    else:
                        print(player.name + " Loose by crash")
                        self.players.remove(player)
                else:
                    print(player.name + " Loose by falling off")
                    self.players.remove(player)

            elif orient == "up":
                if player.position[1] - 1 >= 0:
                    if self.mappositions[player.position[0]][player.position[1] - 1] == 0:
                        self.MoveUp(surface, player)
                    elif player.AI == True and self.mappositions[player.position[0]][player.position[1] - 1] != 1 and self.mappositions[player.position[0]][player.position[1] - 1] != player.playerid:
                        self.MoveUp(surface, player)
                    else:
                        print(player.name + " Loose by crash")
                        self.players.remove(player)
                else:
                    print(player.name + " Loose by falling off")
                    self.players.remove(player)

            elif orient == "down":
                if player.position[1] + 1 < self.dimention:
                    if self.mappositions[player.position[0]][player.position[1] + 1] == 0:
                        self.MoveDown(surface, player)
                    elif player.AI == True and self.mappositions[player.position[0]][player.position[1] + 1] != 1 and self.mappositions[player.position[0]][player.position[1] + 1] != player.playerid:
                        self.MoveDown(surface, player)
                    else:
                        print(player.name + " Loose by crash")
                        self.players.remove(player)
                else:
                    print(player.name + " Loose by falling off")
                    self.players.remove(player)

    def MoveUp(self, surface, player):
        self.mappositions[player.position[0]][player.position[1] - 1] = player.playerid
        player.position[1] -= 1
        x = player.position[0]*self.dimention
        y = player.position[1]*self.dimention
        pygame.draw.rect(surface, player.color, (x, y, self.dimention, self.dimention))
        
    def MoveDown(self, surface, player):
        self.mappositions[player.position[0]][player.position[1] + 1] = player.playerid
        player.position[1] += 1
        x = player.position[0]*self.dimention
        y = player.position[1]*self.dimention
        pygame.draw.rect(surface, player.color, (x, y, self.dimention, self.dimention))
    
    def MoveLeft(self, surface, player):
        self.mappositions[player.position[0] - 1][player.position[1]] = player.playerid
        player.position[0] -= 1
        x = player.position[0]*self.dimention
        y = player.position[1]*self.dimention
        pygame.draw.rect(surface, player.color, (x, y, self.dimention, self.dimention))
    
    def MoveRight(self, surface, player):
        self.mappositions[player.position[0] + 1][player.position[1]] = player.playerid
        player.position[0] += 1
        x = player.position[0]*self.dimention
        y = player.position[1]*self.dimention
        pygame.draw.rect(surface, player.color, (x, y, self.dimention, self.dimention))
