#! /usr/bin/env python

import json
import pygame


# Sets the defaults for the player
class Player(object):

    def __init__(self, pos):
        self.position = (pos[0], pos[1])
        self.rect = pygame.Rect(self.position[0], self.position[1], 32, 32)

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
        # move to next level
        if self.rect.colliderect(exitdoor.rect):
            nextlvl()

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:                            # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0:                            # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0:                            # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0:                            # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom


# Load and prep the games mapping section
class Gamemap:
    def __init__(self):
        with open(f"maps/lvls.json") as mapdata:
            worldmap = json.load(mapdata)
        self.currentlvl = 0
        self.playerstart = worldmap["levels"][0]["lvldata"][0]["playerstart"]
        self.tilemap = worldmap["levels"][0]["lvldata"][1]["tilemap"]
        self.exitdoor = worldmap["levels"][0]["lvldata"][2]["exitdoor"]


# Create the wall objects for the map creation
class Wall(object):

    def __init__(self, pos):
        walls.append(self)                                # Adding the walls to the walls list for easy access
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)   # Creates a collide-able rectangle for the wall


# Create the door object for going between maps
class Door(object):

    def __init__(self, pos):
        doors.append(self)                                # Adding the door to the doors list for easy access
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)   # Creates a collide-able rectangle for the door


# Loads the next level of the game
def nextlvl():
    screen.blit(background_image, [0, 0])                                                       # Redraws the background across the games screen
    Gamelvl.currentlvl += 1                                                                     # Changes the level selector
    with open(f"maps/lvls.json") as mapdata:                                                    # Re-loads the map data
        worldmap = json.load(mapdata)                                                           # Getting the map data ready to use
    Gamelvl.playerstart = worldmap["levels"][Gamelvl.currentlvl]["lvldata"][0]["playerstart"]   # Updating the levels player start location from map data
    Gamelvl.tilemap = worldmap["levels"][Gamelvl.currentlvl]["lvldata"][1]["tilemap"]           # Updating the levels tilemap from map data
    Gamelvl.exitdoor = worldmap["levels"][Gamelvl.currentlvl]["lvldata"][2]["exitdoor"]         # Updating the levels exit door location from map data
    lvlpreload()
    lvldraw()
    player.position = Gamelvl.playerstart                                                       # Sets the players position to the new starting location
    screen.blit(playersprite, player)                                                           # Draws the character to the screen
    pygame.display.update()                                                                     # Renders all updates on the screen


# Creates environment objects from the levels tilemap
# W = wall
def lvlpreload():
    x = y = 0
    for row in Gamelvl.tilemap:
        for col in row:
            if col == "W":
                Wall((x, y))
            x += 32
        y += 32
        x = 0


# Draws the environment objects on the screen
def lvldraw():
    for Wall in walls:
        wallsprite = pygame.image.load('pics/wall.png').convert()
        screen.blit(wallsprite, Wall)
    for x in doors:
        nextdoor = pygame.image.load('pics/nextdoor.png').convert()
        screen.blit(nextdoor, x)



# Set up the game for the first time
pygame.init()
pygame.display.set_caption("Caseys game")       # Title of the games display window
screen = pygame.display.set_mode((1600, 900))   # Create the games display and set it to 1600x900
clock = pygame.time.Clock()                     # Getting the clock ready
FPS = 60                                        # Setting the target frames per second
clock.tick(FPS)                                 # Starting the games internal clock
doors = []                                      # List to hold the doors
walls = []                                      # List to hold the walls
Gamelvl = Gamemap()                             # Creates the first Gamelvl object
lvlpreload()
player = Player(Gamelvl.playerstart)            # Create the player object
exitdoor = Door(Gamelvl.exitdoor)               # Create the levels exit door

########## Starting the game loop ##########

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-3, 0)
    if key[pygame.K_RIGHT]:
        player.move(3, 0)
    if key[pygame.K_UP]:
        player.move(0, -3)
    if key[pygame.K_DOWN]:
        player.move(0, 3)

    # Draw the scene
    background_image = pygame.image.load('pics/floor.png').convert()
    screen.blit(background_image, [0, 0])
    lvldraw()
    playersprite = pygame.image.load('pics/player.png').convert()
    screen.blit(playersprite, player)
    pygame.display.update()
pygame.quit()
