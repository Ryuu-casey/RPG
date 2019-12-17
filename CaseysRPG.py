#!/user/bin/python3
"""

This is the front end of the application


"""
import pygame
from gamemap import gamemap
from config import FPS, screensize, gamestartlvl
from player import Player

pygame.init()
gameDisplay = pygame.display.set_mode(screensize)
clock = pygame.time.Clock()  # Getting the clock ready
clock.tick(FPS)  # Starting the games internal clock and setting the frames per second
Gamelvl = gamemap(gamestartlvl)  # Creates the first Gamelvl object
Gamelvl.lvlpreload()
playerone = Player(Gamelvl.playerstart)  # Create the player object
from items import Sword
playerone.inventory.Weapon.append(Sword)

# Starting the game loop #
def main():
    from config import gamerunning
    while gamerunning is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamerunning = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                gamerunning = False

        # Move the player if an arrow key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            playerone.move(-4, 0)
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            playerone.move(4, 0)
        if key[pygame.K_UP] or key[pygame.K_w]:
            playerone.move(0, -4)
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            playerone.move(0, 4)

        # if key[pygame.MOUSEBUTTONDOWN]:
        #     from rgbcolor import darkred
        #     import player
        #     slash = pygame.draw.rect(gamestartlvl, darkred, playerone.rect)
        #     playerone.do_attack()

        # Draw the scene
        from config import backgroundImage
        gameDisplay.blit(backgroundImage, [0, 0])
        Gamelvl.lvldraw()
        gameDisplay.blit(playerone.playersprite, playerone)
        pygame.display.update()


if __name__ == "__main__":
    main()
