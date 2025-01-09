# Maria Clara Canuto Gontijo - 232005352

import pygame
import math

from classes import BasicTask, unlockText, Helper
from save_sys import SaveSystem

pygame.init()

SCREEN_W = 650
SCREEN_H = 750

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('Robs Petter')

framerate = 60
game_fontBIG = pygame.font.Font('freesansbold.ttf', 25)
game_font = pygame.font.Font('freesansbold.ttf', 16)
run = True
colorText = (211, 219, 224)
timer = pygame.time.Clock()

save = SaveSystem()

save.load_game()
game_data = save.get_data()

coins = game_data['coins']
flag = game_data['flag']
draw1 = game_data['task1Progress']
draw2 = game_data['task2Progress']
draw3 = game_data['task3Progress']
draw4 = game_data['task4Progress']
leng1 = game_data['leng1']
leng2 = game_data['leng2']
leng3 = game_data['leng3']
leng4 = game_data['leng4']

owned1 = game_data['owned1']
owned2 = game_data['owned2']
owned3 = game_data['owned3']
owned4 = game_data['owned4']

coord_y = (SCREEN_H / 6)
robs = pygame.image.load('img/RobsPetMe.png')
robsRect = robs.get_rect(topleft = (50, coord_y))

animating = False
animation_time = 0
bounce_amplitude = 20

def createTask(type, leng, draw, coins):
    Icon_button = type.icon()
    leng, draw, coins = type.box(game_font, leng, draw, coins)
    return Icon_button, leng, draw, coins

type1 = BasicTask(screen, 120, 'Dar Petisco', 2, 1.5)
type2 = BasicTask(screen, 120 + 70, 'Brincar', 4, 1)
type3 = BasicTask(screen, 120 + 140, 'Dar Manga', 6, 0.75)
type4 = BasicTask(screen, 120 + 210, 'Passear', 10, 0.5)

tasks = [
    {'type': type1, 'flag': 25, 'draw': draw1, 'leng': leng1},
    {'type': type2, 'flag': 50, 'draw': draw2, 'leng': leng2},
    {'type': type3, 'flag': 100, 'draw': draw3, 'leng': leng3},
    {'type': type4, 'flag': 210, 'draw': draw4, 'leng': leng4}
]

for i, task in enumerate(tasks):
    if coins >= task['flag'] and flag <= i:
        flag = i + 1
        task['type'], task['leng'], task['draw'], coins = createTask(
            task['type'], task['draw'], task['leng'], coins
        )

def createHelper(type, font, name, coins, cost, check, owned):
    helpicon = type.iconHelp(font, name)
    coins, cost, check, owned = type.workHelp(font, coins, cost, check, owned)
    return helpicon, coins, cost, check, owned

helpType1 = Helper(screen, 70)
helpType2 = Helper(screen, 190)
helpType3 = Helper(screen, 310)
helpType4 = Helper(screen, 435)

helpers = [
    {'helperType': helpType1, 'flag': 250, 'cost': 350, 'image': None, 'owned': owned1, 'check': False},
    {'helperType': helpType2, 'flag': 400, 'cost': 500, 'image': None, 'owned': owned2, 'check': False},
    {'helperType': helpType3, 'flag': 700, 'cost': 850, 'image': None, 'owned': owned3, 'check': False},
    {'helperType': helpType4, 'flag': 900, 'cost': 1000, 'image': None, 'owned': owned4, 'check': False}
]

for j, helper in enumerate(helpers):
    if coins >= helper['flag'] and flag <= j:
        flag = j + 1
        helper['helperType'], helper['cost'], helper['image'], helper['owned'], helper['check'], coins = createTask(
            helper['helperType'], helper['cost'], helper['image'], helper['owned'], helper['check'], coins
        )

def score():
    score_display = game_fontBIG.render(f"Robinhos: " + str(round(coins, 2)), True, colorText)
    screen.blit(score_display, (100, 70))

    coins_image = pygame.image.load('img/RobsCoin.png')
    coins_image = pygame.transform.scale(coins_image, (40, 40))
    
    screen.blit(coins_image, (50, 60))

while run:

    timer.tick(framerate)

    screen.fill((84, 46, 24))
    screen.blit(robs, robsRect.topleft)

    pygame.draw.rect(screen, (77, 37, 19), [350, 0, 500, SCREEN_H])
    pygame.draw.rect(screen, (48, 23, 11), [0, 525, SCREEN_W, 350])
    pygame.draw.rect(screen, (64, 36, 22), [0, 485, SCREEN_W, 65])

    if coins >= 25 and flag == 0:
        flag = 1

    elif coins >= 50 and flag == 1:
        flag = 2

    elif coins >= 100 and flag == 2:
        flag = 3

    elif coins >= 210 and flag == 3:
        flag = 4

    elif coins >= 250 and flag == 4:
        flag = 5

    elif coins >= 300 and flag == 5:
        flag = 6

    elif coins >= 450 and flag == 6:
        flag = 7

    elif coins >= 600 and flag == 7:
        flag = 8

    add = unlockText(screen, coins)

    if flag == 0:
        add.Writetext("Robs é um cachorrinho muito amado que adora carinho!", game_font, 110, 500, False, 15, 0)
        add.Writetext("Clique nesse bobo para fazer carinho nele e ganhar Robinhos!", game_font, 85, 520, False, 15, 0)

    elif flag == 0:
        add.Writetext("Parece que você pegou o jeito! Continue clicando para obter as Tarefas!", game_font, 50, 500, True, 15, 20)

    elif flag == 1:
        add.Writetext("As Tarefas são pequenas atividades que lhe dão Robinhos. Tente usá-las!", game_font, 40, 500, True, 24, 50)

    elif flag == 5:
        add.Writetext("Contrate ajudantes para automatizar as tarefas!", game_font, 125, 510, True, 250, 350)

    score()

    if flag >= 1:

        title = game_fontBIG.render('Tarefas', True, colorText)
        screen.blit(title, (450, 45))

        task1, leng1, draw1, coins = createTask(type1, leng1, draw1, coins)
        
        if owned1 and not draw1:
            draw1 = True


    if flag >= 2:
        task2, leng2, draw2, coins = createTask(type2, leng2, draw2, coins)

        if owned2 and not draw2:
            draw2 = True

    if flag >= 3:
        task3, leng3, draw3, coins = createTask(type3, leng3, draw3, coins)

        if owned3 and not draw3:
            draw3 = True

    if flag >= 4:
        task4, leng4, draw4, coins = createTask(type4, leng4, draw4, coins)

        if owned4 and not draw4:
            draw4 = True

    if flag >= 5:

        title2 = game_fontBIG.render('Ajudantes', True, colorText)
        screen.blit(title2, (70 - 50, 560))

        helper1, coins, cost1, check1, owned1 = createHelper(helpType1, game_font, 'Chuchu', coins, 350, False, owned1)

    if flag >= 6:
        helper2, coins, cost2, check2, owned2 = createHelper(helpType2, game_font, 'Gato Maluco', coins, 500, False, owned2)
        
    if flag >= 7:
        helper3, coins, cost3, check3, owned3 = createHelper(helpType3, game_font, 'Mangueira', coins, 850, False, owned3)

    if flag >= 8:
        helper4, coins, cost4, check4, owned4 = createHelper(helpType4, game_font, 'Guia Mágica', coins, 1000, False, owned4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if robsRect.collidepoint(event.pos):
                animating = True
                animation_time = 0
                coins += 1
            
            if flag >= 1 and task1.collidepoint(event.pos):
                draw1 = True

            elif flag >= 1 and owned1:
                draw1 = True
            
            if flag >= 2 and task2.collidepoint(event.pos):
                draw2 = True
            
            if flag >= 3 and task3.collidepoint(event.pos):
                draw3 = True
 
            if flag >= 4 and task4.collidepoint(event.pos):
                draw4 = True

            elif flag >= 5 and helper1.collidepoint(event.pos):
                if coins >= cost1 and check1 and not owned1:
                    owned1 = True
                    coins -= cost1

            elif flag >= 6 and helper2.collidepoint(event.pos):
                if coins >= cost2 and check2 and not owned2:
                    owned2 = True
                    coins -= cost2

            elif flag >= 7 and helper3.collidepoint(event.pos):
                if coins >= cost3 and check3 and not owned3:
                    owned3 = True
                    coins -= cost3

            elif flag >= 8 and helper4.collidepoint(event.pos):
                if coins >= cost4 and check4 and not owned4:
                    owned4 = True
                    coins -= cost4

            save.update(coins, flag, draw1, draw2, draw3, draw4, leng1, leng2, leng3, leng4, owned1, owned2, owned3, owned4)


    if animating:
        animation_time += 1
        offset = bounce_amplitude * abs(math.sin(animation_time * 0.1))
        robsRect.y = coord_y - offset

        if animation_time > 30:
            animating = False
            robsRect.y = coord_y

    save.update(coins, flag, draw1, draw2, draw3, draw4, leng1, leng2, leng3, leng4, owned1, owned2, owned3, owned4)

    pygame.display.flip()

pygame.quit()