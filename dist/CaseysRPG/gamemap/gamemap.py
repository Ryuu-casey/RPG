#!/usr/bin/python3

"""

This is to handle the games mapping system using my API

"""

import json
import pygame

background_image = pygame.image.load("./pics/floor.png")

class gamemap(object):
    def __init__(self, gamestartlvl):
        with open(f"./maps/lvls03.json") as mapdata:
            worldmap = json.load(mapdata)
        self.currentlvl = gamestartlvl
        self.playerstart = worldmap[self.currentlvl]["playerstart"]
        self.tilemap = worldmap[self.currentlvl]["tilemap"]
        self.doorways = worldmap[self.currentlvl]["doorways"]

    # Loads the next level of the game
    def nextlvl(self):
        from CaseysRPG import gameDisplay
        from config import config
        for door in config.doors:
            self.currentlvl = door.leadsto  # Sets the current level to wherever the door leads to
        gameDisplay.fill((255, 255, 255))  # Wipes the screen to load the new level
        gameDisplay.blit(background_image, [0, 0])  # Redraws the background across the games screen
        config.doors.clear()  # Clears out the doors from the previous level
        config.walls.clear()  # Clears out the walls from the previous level
        with open(f"./maps/lvls03.json") as mapdata:  # Re-loads the map data
            worldmap = json.load(mapdata)  # Getting the map data ready to use
        self.playerstart = worldmap[self.currentlvl]["playerstart"]  # Loads the new levels player start location
        self.tilemap = worldmap[self.currentlvl]["tilemap"]  # Loads the new levels tile map
        self.doorways = worldmap[self.currentlvl]["doorways"]  # Loads the new levels doors
        self.lvlpreload()
        self.lvldraw()

    # Creates environment objects from the current level
    # W = wall
    def lvlpreload(self):
        x = y = 0
        for row in self.tilemap:
            for col in row:
                if col == "W":
                    Wall((x, y))
                x += 32
            y += 32
            x = 0
        for mpdoors in self.doorways:
            if mpdoors:
                Door(mpdoors)

    # Draws the environment objects on the screen
    def lvldraw(self):
        from config import config
        from CaseysRPG import gameDisplay
        for Wall in config.walls:
            wallsprite = pygame.image.load('./pics/wall.png').convert()
            gameDisplay.blit(wallsprite, Wall)
        for Door in config.doors:
            gameDisplay.blit(Door.doorpic, Door)


class Wall(object):

    def __init__(self, pos):
        from config import config
        config.walls.append(self)  # Adding the walls to the walls list for easy access
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)  # Creates a collide-able rectangle for the wall


class Door(object):

    def __init__(self, doornumb):
        from config import config
        from CaseysRPG import Gamelvl
        self.doorpic = pygame.image.load("./pics/nextdoor.png").convert()
        with open(f"./maps/lvls03.json") as mapdata:
            worldmap = json.load(mapdata)
        config.doors.append(self)  # Adding the door to the doors list for easy access
        self.location = worldmap[Gamelvl.currentlvl]["doorways"][doornumb]["loconmap"]  # Location on map for this door
        self.rect = pygame.Rect(self.location[0], self.location[1], 32, 32)  # Creates a collide-able rectangle for the door
        self.leadsto = worldmap[Gamelvl.currentlvl]["doorways"][doornumb]["leadsto"]  # Where this door goes