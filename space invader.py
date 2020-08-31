import random

import pygame

import math

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, 24)

caption = pygame.display.set_caption("solar invader")

backgroundIMG = pygame.image.load(
    "space-cartoon-background-planets-creative-art-space-cartoon-space-background"
    "-besthqwallpapers.com-1366x768.jpg")

icon = pygame.image.load("planet.png")
pygame.display.set_icon(icon)
playerIMG = pygame.image.load('spaceship (4).png')

playerX = 650
playerY = 650
playerX_change = 0

enemyIMG = pygame.image.load('saturn.png')

enemyX = random.randint(0, 1300)
enemyY = random.randint(50, 160)
enemyX_change = 16
enemyY_change = 75

enemyIMG2 = pygame.image.load('jupiter.png')

enemyX2 = random.randint(0, 1300)
enemyY2 = random.randint(30, 140)
enemyX_change2 = 19
enemyY_change2 = 90

enemyIMG3 = pygame.image.load('neptune.png')

enemyX3 = random.randint(0, 1300)
enemyY3 = random.randint(40, 150)
enemyX_change3 = 15
enemyY_change3 = 70

enemyIMG4 = pygame.image.load('venus (1).png')

enemyX4 = random.randint(0, 1300)
enemyY4 = random.randint(40, 150)
enemyX_change4 = 15
enemyY_change4 = 55

bulletIMG = pygame.image.load("bowling-ball.png")
bulletX = 600
bulletY = 650
bulletX_change = 0
bulletY_change = 60
bullet_state = "ready"


def enemy():
    screen.blit(enemyIMG, (enemyX, enemyY))


def enemy2():
    screen.blit(enemyIMG2, (enemyX2, enemyY2))


def enemy3():
    screen.blit(enemyIMG3, (enemyX3, enemyY3))


def enemy4():
    screen.blit(enemyIMG4, (enemyX4, enemyY4))


def player():
    screen.blit(playerIMG, (playerX, playerY))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIMG, (x, y))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    X = enemyX
    Y = enemyY
    Xi = bulletX
    Yi = bulletY
    distance = math.sqrt((X - Xi) ** 2 + (Y - Yi) ** 2)
    if distance < 60:
        return True
    else:
        return False


def iscollision2(enemyX2, enemyY2, bulletX, bulletY):
    X2 = enemyX2
    Y2 = enemyY2
    Xi = bulletX
    Yi = bulletY
    distance = math.sqrt((X2 - Xi) ** 2 + (Y2 - Yi) ** 2)
    if distance < 60:
        return True
    else:
        return False


def iscollision3(enemyX3, enemyY3, bulletX, bulletY):
    X3 = enemyX3
    Y3 = enemyY3
    Xi = bulletX
    Yi = bulletY
    distance = math.sqrt((X3 - Xi) ** 2 + (Y3 - Yi) ** 2)
    if distance < 60:
        return True
    else:
        return False


def iscollision4(enemyX4, enemyY4, bulletX, bulletY):
    X4 = enemyX4
    Y4 = enemyY4
    Xi = bulletX
    Yi = bulletY
    distance = math.sqrt((X4 - Xi) ** 2 + (Y4 - Yi) ** 2)
    if distance < 60:
        return True
    else:
        return False


score_value = 0
font = pygame.font.Font("freesansbold.ttf", 50)
textX = 15
textY = 15

over_value = 0
over_font = pygame.font.Font("freesansbold.ttf", 5000)
line_font = pygame.font.Font("freesansbold.ttf", 150)
lost_font = pygame.font.Font("freesansbold.ttf", 5000)


def show_score(x, y):
    score = font.render("SCORE=" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def line(x, y):
    line = font.render("=================================================="
                       "===================================================", True, (255, 255, 255))
    screen.blit(line, (x, y))


def lost(x, y):
    you_lost = font.render("YOU LOSE!", True, (255, 255, 255))
    screen.blit(you_lost, (x, y))


def game_over():
    over = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over, (550, 250))


running = True
while running:

    screen.fill((0, 0, 30))

    screen.blit(backgroundIMG, [0, 0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -30

            if event.key == pygame.K_RIGHT:
                playerX_change = 30

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    bulletX += 53
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    if playerX <= 20:
        playerX = 20

    if playerX >= 1200:
        playerX = 1200

    if enemyX <= 0:
        enemyX = 0
        enemyX_change = 18
        enemyY += enemyY_change

    if enemyX >= 1300:
        enemyX = 1300
        enemyX_change = -18
        enemyY += enemyY_change

    if enemyX2 <= 0:
        enemyX2 = 0
        enemyX_change2 = 16
        enemyY2 += enemyY_change2

    if enemyX2 >= 1300:
        enemyX2 = 1300
        enemyX_change2 = -19
        enemyY2 += enemyY_change2

    if enemyX3 <= 0:
        enemyX3 = 0
        enemyX_change3 = 15
        enemyY3 += enemyY_change3

    if enemyX3 >= 1300:
        enemyX3 = 1300
        enemyX_change3 = -15
        enemyY3 += enemyY_change3

    if enemyX4 <= 0:
        enemyX4 = 0
        enemyX_change4 = 20
        enemyY4 += enemyY_change4

    if enemyX4 >= 1300:
        enemyX4 = 1300
        enemyX_change4 = -17
        enemyY4 += enemyY_change4

    if bulletX <= 16:
        bulletX = 16

    if bulletX >= 1300:
        bulletX = 1300

    if bulletY <= 0:
        bulletY = 650
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    collision = iscollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 650
        bullet_state = "ready"
        enemyY = random.randint(50, 150)
        enemyX = random.randint(0, 1300)
        score_value += 1

    collision2 = iscollision2(enemyX2, enemyY2, bulletX, bulletY)
    if collision2:
        bulletY = 650
        bullet_state = "ready"
        enemyY2 = random.randint(50, 140)
        enemyX2 = random.randint(0, 1300)
        score_value += 1

    collision3 = iscollision3(enemyX3, enemyY3, bulletX, bulletY)
    if collision3:
        bulletY = 650
        bullet_state = "ready"
        enemyY3 = random.randint(50, 170)
        enemyX3 = random.randint(0, 1300)
        score_value += 1

    collision4 = iscollision4(enemyX4, enemyY4, bulletX, bulletY)
    if collision4:
        bulletY = 650
        bullet_state = "ready"
        enemyY4 = random.randint(50, 170)
        enemyX4 = random.randint(0, 1300)
        score_value += 1
    overX = 200
    overY = 250
    lostX = 565
    lostY = 350

    if enemyY > 550:
        enemyY = 5000
        enemyX = 5000
        enemyY2 = 5000
        enemyX2 = 5000
        enemyY3 = 5000
        enemyX3 = 5000
        enemyX4 = 5000
        enemyY4 = 5000
        bulletY = 6000
        playerX_change = 0
        playerX = 650
        game_over()
        lost(lostX, lostY)

    if enemyY2 > 550:
        enemyY = 5000
        enemyX = 5000
        enemyY2 = 5000
        enemyX2 = 5000
        enemyY3 = 5000
        enemyX3 = 5000
        enemyX4 = 5000
        enemyY4 = 5000
        bulletY = 6000
        playerX_change = 0
        playerX = 650
        game_over()
        lost(lostX, lostY)

    if enemyY3 > 550:
        enemyY = 5000
        enemyX = 5000
        enemyY2 = 5000
        enemyX2 = 5000
        enemyY3 = 5000
        enemyX3 = 5000
        enemyX4 = 5000
        enemyY4 = 5000
        bulletY = 6000
        playerX_change = 0
        playerX = 650
        game_over()
        lost(lostX, lostY)

    if enemyY4 > 550:
        enemyY = 5000
        enemyX = 5000
        enemyY2 = 5000
        enemyX2 = 5000
        enemyY3 = 5000
        enemyX3 = 5000
        enemyX4 = 5000
        enemyY4 = 5000
        bulletY = 6000
        playerX_change = 0
        playerX = 650
        game_over()
        lost(lostX, lostY)

    enemyX += enemyX_change
    enemyX2 += enemyX_change2
    enemyX3 += enemyX_change3
    enemyX4 += enemyX_change4
    playerX += playerX_change
    bulletX += bulletX_change

    player()
    show_score(textX, textY)
    line(-5, 605)
    enemy()
    enemy2()
    enemy3()
    enemy4()

    pygame.display.update()
