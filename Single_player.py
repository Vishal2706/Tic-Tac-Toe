import pygame
import pygame.locals
import numpy as np
from sklearn import neighbors
import pickle

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.draw.rect(screen, (100, 150, 50), (100, 50, 600, 500))
pygame.draw.rect(screen, (100, 0, 0), [150, 100, 500, 400], 2)
pygame.draw.line(screen, (255, 50, 30), (300, 100), (300, 500), 2)
pygame.draw.line(screen, (255, 50, 30), (500, 100), (500, 500), 2)
pygame.draw.line(screen, (100, 10, 30), (150, 220), (650, 220), 2)
pygame.draw.line(screen, (100, 10, 30), (150, 370), (650, 370), 2)

auto = pickle.load(open("train_model.train", "rb"))


def message(txt, s, c):
    font = pygame.font.SysFont("Times New Roman, Arial", s)
    text = font.render(txt, True, c)
    return text


def label(s):
    pygame.draw.rect(screen, (0, 0, 0), [0, 0, 150, 50])
    p1 = message(s, 30, (50, 10, 20))
    screen.blit(p1, (10, 10))
    pygame.display.update()


a = np.zeros((3, 3), dtype=np.int8)



def motion():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP7]:
        if a[0][0] == 0:
            a[0][0] = 1
            star = message('*', 90, (255, 0, 0))
            screen.blit(star, (200, 135))
            return True

    if keys[pygame.K_KP8]:
        if a[0][1] == 0:
            a[0][1] = 1
            star = message('*', 90, (255, 0, 0))
            screen.blit(star, (380, 135))
            return True

    if keys[pygame.K_KP9]:
        if a[0][2] == 0:
            a[0][2] = 1
            star = message('*', 90, (255, 0, 0))
            screen.blit(star, (550, 135))
            return True

    if keys[pygame.K_KP4]:
        if a[1][0] == 0:
            a[1][0] = 1
            star = message('*', 90, (255, 0, 0))
            screen.blit(star, (200, 270))
            return True

    if keys[pygame.K_KP5]:
        if a[1][1] == 0:
            a[1][1] = 1
            star = message('*', 90, (255, 0, 0))
            screen.blit(star, (380, 270))
            return True

    if keys[pygame.K_KP6]:
        if a[1][2] == 0:
            a[1][2] = 1
            star = message('*', 90, (255, 0, 0))
            screen.blit(star, (550, 270))
            return True

    if keys[pygame.K_KP1]:
        if a[2][0] == 0:
            a[2][0] = 1
            star = message('*', 90, (255, 0, 0))
            screen.blit(star, (200, 410))
            return True

    if keys[pygame.K_KP2]:
        if a[2][1] == 0:
            a[2][1] = 1
            star = message('*', 90, (255, 0, 0))
            screen.blit(star, (380, 410))
            return True

    if keys[pygame.K_KP3]:
        if a[2][2] == 0:
            a[2][2] = 1
            star = message('*', 90, (255, 0, 0))
            screen.blit(star, (550, 410))
            return True
    validation()


def computer():
    k = a.flatten().reshape((1, 9))
    k = k.reshape(len(k), -1)
    pred = auto.predict(k)

    if pred == 0:
        if a[0][0] == 0:
            a[0][0] = -1
            star = message('0', 90, (255, 0, 0))
            screen.blit(star, (200, 135))
            return True

    if pred == 1:
        if a[0][1] == 0:
            a[0][1] = -1
            star = message('0', 90, (255, 0, 0))
            screen.blit(star, (380, 135))
            return True

    if pred == 2:
        if a[0][2] == 0:
            a[0][2] = -1
            star = message('0', 90, (255, 0, 0))
            screen.blit(star, (550, 135))
            return True

    if pred == 3:
        if a[1][0] == 0:
            a[1][0] = -1
            star = message('0', 90, (255, 0, 0))
            screen.blit(star, (200, 270))
            return True

    if pred == 4:
        if a[1][1] == 0:
            a[1][1] = -1
            star = message('0', 90, (255, 0, 0))
            screen.blit(star, (380, 270))
            return True

    if pred == 5:
        if a[1][2] == 0:
            a[1][2] = -1
            star = message('0', 90, (255, 0, 0))
            screen.blit(star, (550, 270))
            return True

    if pred == 6:
        if a[2][0] == 0:
            a[2][0] = -1
            star = message('0', 90, (255, 0, 0))
            screen.blit(star, (200, 410))
            return True

    if pred == 7:
        if a[2][1] == 0:
            a[2][1] = -1
            star = message('0', 90, (255, 0, 0))
            screen.blit(star, (380, 410))
            return True

    if pred == 8:
        if a[2][2] == 0:
            a[2][2] = -1
            star = message('0', 90, (255, 0, 0))
            screen.blit(star, (550, 410))
            return True


def validation():
    if a[0][0] == -1 and a[0][1] == -1 and a[0][2] == -1:
        mgs = message("Computer won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))

    if a[1][0] == -1 and a[1][1] == -1 and a[1][2] == -1:
        mgs = message("Computer won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[2][0] == -1 and a[2][1] == -1 and a[2][2] == -1:
        mgs = message("Computer won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))

    if a[0][0] == 1 and a[0][1] == 1 and a[0][2] == 1:
        mgs = message("you won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[1][0] == 1 and a[1][1] == 1 and a[1][2] == 1:
        mgs = message("you won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[2][0] == 1 and a[2][1] == 1 and a[2][2] == 1:
        mgs = message("you won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))

    if a[0][0] == -1 and a[1][0] == -1 and a[2][0] == -1:
        mgs = message("computer won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[0][1] == -1 and a[1][1] == -1 and a[2][1] == -1:
        mgs = message("computer won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[0][2] == -1 and a[1][2] == -1 and a[2][2] == -1:
        mgs = message("computer won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))

    if a[0][0] == 1 and a[1][0] == 1 and a[2][0] == 1:
        mgs = message("you won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[0][1] == 1 and a[1][1] == 1 and a[2][1] == 1:
        mgs = message("you won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[0][2] == 1 and a[1][2] == 1 and a[2][2] == 1:
        mgs = message("you won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))

    if a[0][0] == -1 and a[1][1] == -1 and a[2][2] == -1:
        mgs = message("computer won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[0][0] == 1 and a[1][1] == 1 and a[2][2] == 1:
        mgs = message("you won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))

    if a[0][2] == -1 and a[1][1] == -1 and a[2][0] == -1:
        mgs = message("computer won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))
    if a[0][2] == 1 and a[1][1] == 1 and a[2][0] == 1:
        mgs = message("you won", 60, (100, 100, 100))
        screen.blit(mgs, (400, 400))


flag = 0
count = 0
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            exit(1)
        if flag == 0:
            label("player 1")
            if motion():
                validation()
                count += 1
                if count == 9:
                    screen.blit(message("Game tie", 82, (255, 0, 0)), (200, 300))
                print(count)
                flag = 1

        if flag == 1:
            label("computer")
            if computer():
                validation()
                count += 1
                if count == 9:
                    screen.blit(message("Game tie", 82, (255, 0, 0)), (200, 300))
                print(count)
                flag = 0


        pygame.display.update()
