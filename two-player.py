import pygame
import pygame.locals

a = [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
screen = pygame.display.set_mode((800, 600))
pygame.draw.rect(screen, (100, 150, 50), (100, 50, 600, 500))
pygame.draw.rect(screen, (100, 0, 0), [150, 100, 500, 400], 2)
pygame.draw.line(screen, (255, 50, 30), (300, 100), (300, 500), 2)
pygame.draw.line(screen, (255, 50, 30), (500, 100), (500, 500), 2)
pygame.draw.line(screen, (100, 10, 30), (150, 220), (650, 220), 2)
pygame.draw.line(screen, (100, 10, 30), (150, 370), (650, 370), 2)
flag = 0
pygame.init()


def message(txt, s, c):
    font = pygame.font.SysFont("Times New Roman, Arial", s)
    text = font.render(txt, True, c)
    return text


while 1:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            exit(1)
    keys = pygame.key.get_pressed()
    if flag == 0:
        pygame.draw.rect(screen, (0, 0, 0), [0, 0, 150, 50])
        p1 = message("PLAYER 1", 30, (50, 10, 20))
        screen.blit(p1, (10, 10))
        pygame.display.update()
    if flag == 0:
        if keys[pygame.K_KP7]:
            if a[0].__getitem__(0) == 10:
                a[0].insert(0, '*')
                star = message('*', 90, (255, 0, 0))
                screen.blit(star, (200, 135))
                flag = 1
        if keys[pygame.K_KP8]:
            if a[0].__getitem__(1) == 10:
                a[0].insert(1, '*')
                star = message('*', 90, (255, 0, 0))
                screen.blit(star, (380, 135))
                flag = 1
        if keys[pygame.K_KP9]:
            if a[0].__getitem__(2) == 10:
                a[0].insert(2, '*')
                star = message('*', 90, (255, 0, 0))
                screen.blit(star, (550, 135))
                flag = 1
        if keys[pygame.K_KP4]:
            if a[1].__getitem__(0) == 10:
                a[1].insert(0, '*')
                star = message('*', 90, (255, 0, 0))
                screen.blit(star, (200, 270))
                flag = 1
        if keys[pygame.K_KP5]:
            if a[1].__getitem__(1) == 10:
                a[1].insert(1, '*')
                star = message('*', 90, (255, 0, 0))
                screen.blit(star, (380, 270))
                flag = 1
        if keys[pygame.K_KP6]:
            if a[1].__getitem__(2) == 10:
                a[1].insert(2, '*')
                star = message('*', 90, (255, 0, 0))
                screen.blit(star, (550, 270))
                flag = 1
        if keys[pygame.K_KP1]:
            if a[2].__getitem__(0) == 10:
                a[2].insert(0, '*')
                star = message('*', 90, (255, 0, 0))
                screen.blit(star, (200, 410))
                flag = 1
                print(flag)
        if keys[pygame.K_KP2]:
            if a[2].__getitem__(1) == 10:
                a[2].insert(1, '*')
                star = message('*', 90, (255, 0, 0))
                screen.blit(star, (380, 410))
                flag = 1
        if keys[pygame.K_KP3]:
            if a[2].__getitem__(2) == 10:
                a[2].insert(2, '*')
                star = message('*', 90, (255, 0, 0))
                screen.blit(star, (550, 410))
                flag = 1

    if flag == 1:
        pygame.draw.rect(screen, (0, 0, 0), [0, 0, 150, 50])
        p1 = message("PLAYER 2", 30, (50, 10, 20))
        screen.blit(p1, (10, 10))
        print('player 2')

    if flag == 1:
        if keys[pygame.K_KP7]:
            if a[0].__getitem__(0) == 10:
                a[0].insert(0, '0')
                z = message('0', 90, (255, 0, 0))
                screen.blit(z, (200, 135))
                flag = 0
        if keys[pygame.K_KP8]:
            if a[0].__getitem__(1) == 10:
                a[0].insert(1, '0')
                z = message('0', 90, (255, 0, 0))
                screen.blit(z, (380, 135))
                flag = 0
        if keys[pygame.K_KP9]:
            if a[0].__getitem__(2) == 10:
                a[0].insert(2, '0')
                z = message('0', 90, (255, 0, 0))
                screen.blit(z, (550, 135))
                flag = 0
        if keys[pygame.K_KP4]:
            if a[1].__getitem__(0) == 10:
                a[1].insert(0, '0')
                z = message('0', 90, (255, 0, 0))
                screen.blit(z, (200, 270))
                flag = 0
        if keys[pygame.K_KP5]:
            if a[1].__getitem__(1) == 10:
                a[1].insert(1, '0')
                z = message('0', 90, (255, 0, 0))
                screen.blit(z, (380, 270))
                flag = 0
        if keys[pygame.K_KP6]:
            if a[1].__getitem__(2) == 10:
                a[1].insert(2, '0')
                z = message('0', 90, (255, 0, 0))
                screen.blit(z, (550, 270))
                flag = 0
        if keys[pygame.K_KP1]:
            if a[2].__getitem__(0) == 10:
                a[2].insert(0, '0')
                z = message('0', 90, (255, 150, 0))
                screen.blit(z, (200, 410))
                flag = 0
                #print flag
        if keys[pygame.K_KP2]:
            if a[2].__getitem__(1) == 10:
                a[2].insert(1, '0')
                z = message('0', 90, (255, 0, 0))
                screen.blit(z, (380, 410))
                flag = 0
        if keys[pygame.K_KP3]:
            if a[2].__getitem__(2) == 10:
                a[2].insert(2, '0')
                z = message('0', 90, (255, 0, 0))
                screen.blit(z, (550, 410))
                flag = 0

    pygame.display.update()

    if a[0].__getitem__(0) == '*' and a[0].__getitem__(1) == '*' and a[0].__getitem__(2) == '*':
        mgs = message("PLAYER 1 won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))

    if a[1].__getitem__(0) == '*' and a[1].__getitem__(1) == '*' and a[1].__getitem__(2) == '*':
        mgs = message("PLAYER 1 won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[2].__getitem__(0) == '*' and a[2].__getitem__(1) == '*' and a[2].__getitem__(2) == '*':
        mgs = message("PLAYER 1 won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))

    if a[0].__getitem__(0) == '0' and a[0].__getitem__(1) == '0' and a[0].__getitem__(2) == '0':
        mgs = message("PLAYER 2 won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[1].__getitem__(0) == '0' and a[1].__getitem__(1) == '0' and a[1].__getitem__(2) == '0':
        mgs = message("PLAYER 2 won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[2].__getitem__(0) == '0' and a[2].__getitem__(1) == '0' and a[2].__getitem__(2) == '0':
        mgs = message("PLAYER 2 won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))

    if a[0].__getitem__(0) == '*' and a[1].__getitem__(0) == '*' and a[2].__getitem__(0) == '*':
        mgs = message("PLAYER 1 won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[0].__getitem__(1) == '*' and a[1].__getitem__(1) == '*' and a[2].__getitem__(1) == '*':
        mgs = message("PLAYER 1 won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[0].__getitem__(2) == '*' and a[1].__getitem__(2) == '*' and a[2].__getitem__(2) == '*':
        mgs = message("PLAYER 1 won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))

    if a[0].__getitem__(0) == '0' and a[1].__getitem__(0) == '0' and a[2].__getitem__(0) == '0':
        mgs = message("PLAYER 2 won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[0].__getitem__(1) == '0' and a[1].__getitem__(1) == '0' and a[2].__getitem__(1) == '0':
        mgs = message("PLAYER 2 won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[0].__getitem__(2) == '0' and a[1].__getitem__(2) == '0' and a[2].__getitem__(2) == '0':
        mgs = message("PLAYER 2 won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))

    if a[0].__getitem__(0) == '*' and a[1].__getitem__(1) == '*' and a[2].__getitem__(2) == '*':
        mgs = message("PLAYER 1 won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[0].__getitem__(0) == '0' and a[1].__getitem__(1) == '0' and a[2].__getitem__(2) == '0':
        mgs = message("PLAYER 2 won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))

    if a[0].__getitem__(2) == '*' and a[1].__getitem__(1) == '*' and a[2].__getitem__(0) == '*':
        mgs = message("PLAYER 1 won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[0].__getitem__(2) == '0' and a[1].__getitem__(1) == '0' and a[2].__getitem__(0) == '0':
        mgs = message("PLAYER 2 won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))

