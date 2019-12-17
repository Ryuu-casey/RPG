import pygame
import json
import urllib.request

# Initialize pygame
pygame.init()

# Game window environment
FPS = 60
window_width = 800
window_height = 600
size = (window_width, window_height)

# Create the game window
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Casey's Game")
icon = pygame.image.load('pics/Icon.png')
pygame.display.set_icon(icon)

# Creating a player
def player(x, y):
    with open("../char/Ryuu", "rw") as charsel:
        chardata = json.load(charsel)

    screen.blit(playerImg, (x, y))








# player attributes
playerImg = pygame.image.load('pics/Player.png')
playerx = 370
playery = 480
playerX_change = 0
playerY_change = 0

# Skellington attributes
skellingtonImg = pygame.image.load('pics/skellington.png')
skellingtonx = 110
skellingtony = 110
skellingtonX_change = 0
skellingtonY_change = 0

# Starting the clock
clock = pygame.time.Clock()

# Playfield background
background_image = pygame.image.load("pics/Background.png")

def skellington(x, y):
    screen.blit(skellingtonImg, (x, y))


# Starting the game loop
running = True
while running:
    clock.tick(FPS)

    # Game loop part 1: Events ########
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -1
        if event.key == pygame.K_RIGHT:
            playerX_change = 1
        if event.key == pygame.K_UP:
            playerY_change = -1
        if event.key == pygame.K_DOWN:
            playerY_change = 1

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            playerY_change = 0

    playerx += playerX_change
    playery += playerY_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 768:
        playerx = 768
    if playery <= 0:
        playery = 0
    elif playery >= 568:
        playery = 568

    screen.blit(background_image, [0, 0])
    player(playerx, playery)
    skellington(skellingtonx, skellingtony)

    # Game loop part 2: Updates ########

    # Game loop part 3: Draw ########
    pygame.display.update()

pygame.quit()
