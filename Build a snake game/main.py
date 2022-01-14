import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((640,660))
foodimg = pygame.image.load('./fruit.png')

pygame.display.set_caption('SNAKE')

# Player
playerPos = [[300, 300], [300, 320], [300, 340]]
dir = 'u'
def player(pos):
    for x in pos:
        pygame.draw.rect(screen, (225, 225, 225), pygame.Rect(x[0], x[1], 20, 20))

# Food
def add_food(x,y):
    screen.blit(foodimg, (x, y))

# Collision between food and snake
def eat(x, y, foodX, foodY):
    if (x == foodX) and (y == foodY):
        return True
    else:
        return False

# Collision between snake body or boundary
def crash(pos):
    l = [pos[x] for x in range(1, len(pos))]
    if pos[0] in l:
        return True
    elif (pos[0][0] >= 620) or (pos[0][0] < 20) or (pos[0][1] >= 620) or (pos[0][1] < 20):
        return True
    else:
        return False

# Game Over text
over_font = pygame.font.Font('freesansbold.ttf',64)
def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255,255,255))
    screen.blit(over_text, (100,250))

foodX = random.randint(1, 30) * 20
foodY = random.randint(1, 30) * 20
eaten = False

score = 0
running = True
while running:

    screen.fill((20,102,37))

    pygame.draw.rect(screen, (22,168,39), pygame.Rect(20, 20, 600, 600))
    pygame.draw.rect(screen, (22,107,107), pygame.Rect(0,640,640,20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dir = 'u'
            elif event.key == pygame.K_DOWN:
                dir = 'd'
            elif event.key == pygame.K_LEFT:
                dir = 'l'
            elif event.key == pygame.K_RIGHT:
                dir = 'r'
            elif event.key == pygame.K_p:
                pause = True
                while pause:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pause = False
                            running = False
                        elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_p):
                            pause = False
                    pause_text = over_font.render('PAUSED', True, (255, 255, 255))
                    screen.blit(pause_text, (200, 250))
                    pygame.display.update()

    playerPos.insert(1,list(playerPos[0]))
    if dir == 'u':
        playerPos[0][1] -= 20
    elif dir == 'd':
        playerPos[0][1] += 20
    elif dir == 'l':
        playerPos[0][0] -= 20
    elif dir == 'r':
        playerPos[0][0] += 20
    if not eaten:
        playerPos.pop()

    if eaten:
        score += 1
        while True:
            foodX = random.randint(1, 30) * 20
            foodY = random.randint(1, 30) * 20
            if [foodX, foodY] not in playerPos:
                break
        eaten = False

    add_food(foodX,foodY)

    end = crash(playerPos)
    if end:
        game_over_text()
        running = False

    player(playerPos)

    eaten = eat(playerPos[0][0], playerPos[0][1], foodX, foodY)

    pygame.display.update()

    time.sleep(0.07)