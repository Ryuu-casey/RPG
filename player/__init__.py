#!/usr/bin/python3

"""

 This is to handle the player in the RPG game

"""

import pygame
import config
from player.inventory import PlayerInventory


class Player(object):


    def __init__(self, pos):
        self.playersprite = pygame.image.load('./pics/player.png').convert()
        self.position = (pos[0], pos[1])
        self.rect = pygame.Rect(self.position[0], self.position[1], 32, 32)
        self.inventory = PlayerInventory()
        self.level = 1
        self.experience = 0
        self.maxhealth = 100
        self.vitality = 20
        self.attack = 20
        self.defense = 20

    def use_potion(self):
        pass

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
        # move to next level
        for door in config.doors:
            from CaseysRPG import Gamelvl
            if self.rect.colliderect(door.rect):
                Gamelvl.nextlvl()
                self.position = Gamelvl.playerstart  # Sets the players position to the new starting location
                self.rect.x = self.position[0]
                self.rect.y = self.position[1]

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in config.walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom


    def do_attack(self):
        from player.inventory import PlayerInventory
        from items import Melee, Ranged
        if isinstance(PlayerInventory.Weapon, Melee):
            self.melee_attack()
        if isinstance(PlayerInventory.Weapon, Ranged):
            self.ranged_attack()

    def melee_attack(self):
        from CaseysRPG import gameDisplay
        from config import mobs
        meleerect = pygame.Rect(self.rect.midright, 32, 4)
        gameDisplay.blit(meleerect)
        if meleerect.colliderect(mobs.rect):
            mobs.health = 0

    def ranged_attack(self):
        from config import mobs
        rangedrect = pygame.Rect(self.rect.midright, 32, 4)
        if rangedrect.colliderect(mobs.rect):
            pass   # calculate and do some damage

