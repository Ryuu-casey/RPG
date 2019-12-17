#!/usr/bin/python3

"""

This is to handle the games enemies

"""

import pygame


class enemies(object):

    def __init__(self, pos):
        from config import mobs
        self.position = (pos[0], pos[1])
        self.rect = pygame.Rect(self.position[0], self.position[1], 32, 32)
        mobs.append(self)
        self.health = 100
        self.alive = True
        self.defense = 20

    def died(self):
        from config import mobs, killed
        if self.health == 0:
            self.alive = False
        if not self.alive:
            mobs.remove(self)
            killed.append(self)

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
        # move to next level

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        from config import walls
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
