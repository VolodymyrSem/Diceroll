import pygame as pg
import random as ran
from function import dices
import sys

pg.init()

size = (600, 400)
screen = pg.display.set_mode(size)
pg.display.set_caption("Dice Roll")

font = pg.font.SysFont(None, 50)
lst6 = []
lst8 = []
lst12 = []


def background():
    screen.fill(pg.Color('white'))
    pg.draw.rect(screen, pg.Color('black'), pg.Rect(50, 125, 150, 150), 5)
    pg.draw.polygon(screen, pg.Color('black'), [(235, 272.5), (325, 125), (415, 272.5)], 5)
    pg.draw.polygon(screen, pg.Color('black'), [(450, 272.5), (425, 198.75), (500, 125), (575, 198.75), (550, 272.5)], 5)
    txt = ["D6", "D8", "D12"]
    for x, i in enumerate(txt):
        i = font.render(i, True, pg.Color('black'))
        width = 107 + (x*193) if x < 2 else 470
        screen.blit(i, pg.Vector2(width, 70))


def diceroll(x, y):
    if x in range(50, 201) and y in range(125, 276):
        num = font.render(str(dices(6)), True, pg.Color('black'))
        if lst6:
            pg.draw.rect(screen, pg.Color('white'), pg.Rect(75, 150, 75, 75))
            screen.blit(num, pg.Vector2(117, 185))
            lst6[0] = num
        else:
            screen.blit(num, pg.Vector2(117, 185))
            lst6.append(num)
    if x in range(235, 415) and y in range(125, 273):
        num = font.render(str(dices(8)), True, pg.Color('black'))
        if lst8:
            pg.draw.rect(screen, pg.Color('white'), pg.Rect(317, 198, 30, 30))
            screen.blit(num, pg.Vector2(317, 198))
            lst8[0] = num
        else:
            screen.blit(num, pg.Vector2(317, 198))
            lst8.append(num)
    if x in range(425, 575) and y in range(125, 273):
        el = str(dices(12))
        num = font.render(el, True, pg.Color('black'))
        if lst12:
            lst12[0] = el
            if len(lst12[0]) == 1:
                pg.draw.rect(screen, pg.Color('white'), pg.Rect(485, 187, 40, 40))
                screen.blit(num, pg.Vector2(494, 187))
            elif len(lst12[0]) == 2:
                pg.draw.rect(screen, pg.Color('white'), pg.Rect(485, 187, 40, 40))
                screen.blit(num, pg.Vector2(485, 187))
        else:
            screen.blit(num, pg.Vector2(494, 187))
            lst12.append(el)


run = True
var = True
while run:
    while var:
        background()
        var = False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit(0)
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            print(f'x:{x}, y:{y}')
            diceroll(x, y)
    pg.display.flip()
