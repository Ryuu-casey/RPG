#!/usr/bin/python3

import json
import pygame


class Player:
    def __init__(self, name):
        with open("blankchar.json") as blnkchar:
            freshchar = json.load(blnkchar)
        self.name = name
        self.location = []
        self.health = 100
        self.alive = True
        self.attack = 10
        self.level = 1
        self.inventory = []

    def roomspawn(self):
        self.location = Gamemap.playerstart




class Gamemap:
    def __init__(self, lvlnumb):
        with open(f"maps/maptst.json") as mapdata:
            worldmap = json.load(mapdata)
        self.lvlid = worldmap["maps"][{lvlnumb}]["lvlid"]
        self.area = worldmap["maps"][{lvlnumb}]["area"]
        self.playerstart = worldmap["maps"][{lvlnumb}]["playerstart"]
        self.tilemap = worldmap["maps"][{lvlnumb}]["tilemap"]

    def loadtile(self, tiletype):
        if tiletype == "floortile":

        elif tiletype == "walltile":

        elif tiletype == "door":

        elif tiletype == "chest":




class Tile:
    def __init__(self):

# Create the map

# add floor

# add walls

# add player

# add door



# adding a wall block

        for wallblk in currentmap["tilemap"]:
            #add block
            block = Block("pics/wall.png"")
            #set location for block
            block.rect.x = 0
            block.rect.y = 0