#!/usr/bin/python3

import pygame

""""

msg= Display text x,y= location w,h= width&height ic= Inactive color ac= Active color 

"""


def button(text, txtcolor, x, y, width, height, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    mousex = mouse[0]
    mousey = mouse[1]
    click = pygame.mouse.get_pressed()
    if x + width > mousex > x and y + height > mousey > y:
        from CaseysRPG import gameDisplay
        pygame.draw.rect(gameDisplay, ac, (x, y, width, height))

        if click[0] == 1 and action is not None:
            action.main()

    else:
        from CaseysRPG import gameDisplay
        pygame.draw.rect(gameDisplay, ic, (x, y, width, height))

    buttonText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = textObj(text, buttonText, txtcolor)
    textRect.center = ((x + (width / 2)), (y + (height / 2)))
    gameDisplay.blit(textSurf, textRect)


def textObj(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
