#!/usr/bin/python3

"""

 This is to handle the player in the RPG game

"""

import pygame
from config import config

from player import inventory


class Player(object):

    def __init__(self, pos):
        self.playersprite = pygame.image.load('./pics/player.png').convert()
        self.position = (pos[0], pos[1])
        self.rect = pygame.Rect(self.position[0], self.position[1], 32, 32)
        self.inventory = inventory

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


    # def attack(self, type):
    #     if self.attack(type=melee):
    #         self.melee_attack()
    #     if self.attack(type=ranged):
    #         self.ranged_attack()
    #
    # def melee_attack(self):
    #     meleerect = pygame.Rect(self.rect.midright, 32, 4)
    #     if meleerect.colliderect(Enemies.rect)
    #         pass   # calculate and do some damage
    #
    # def ranged_attack(self):
    #     rangedrect = pygame.Rect(self.rect.midright, 32, 4)
    #     if rangedrect.colliderect(Enemies.rect)
    #         pass   # calculate and do some damage

