import pygame

pygame.init()

icon = pygame.image.load("./assets/icon.png")
playerimg = pygame.image.load("./assets/elon.png")
glaser = pygame.image.load("./assets/laser.png")
jeff = pygame.image.load("./assets/jeff.png")
ship = pygame.image.load("./assets/ship.png")
empty = pygame.image.load("./assets/emptybar.png")
redhealth = pygame.image.load("./assets/redbar.png")
bluehealth = pygame.image.load("./assets/bluebar.png")

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Elon vs Jeff")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
playerx = 370
playery = 480
xchange = 0
ychange = 0
score = 10
health = {"elon":1000, "jeff":5000}
lase = {"ready":1, "on":0, "count":0}

def player(x, y):
    screen.blit(playerimg, (x, y))

def laser(x, y, glaser):
    glaser = pygame.transform.scale(glaser, (32, y))
    screen.blit(glaser, (x+16, 28))

def enemy(img1, img2):
    screen.blit(img1, (10, 0))
    screen.blit(img2, (352, 20))

def healthbars(health, red, blue):
    redsize = int((health["jeff"]/5000)*650)
    bluesize = int((health["elon"]/1000)*650)
    screen.blit(empty, (50, 5))
    red = pygame.transform.scale(red, (redsize, 13))
    screen.blit(red, (70, 6))
    screen.blit(empty, (50, 580))
    blue = pygame.transform.scale(blue, (bluesize, 13))
    screen.blit(blue, (70, 581))

def ult(emp, red, score):
    redsize = int((score/30)*200)
    emp = pygame.transform.scale(emp, (210, 6))
    red = pygame.transform.scale(red, (redsize, 3))
    screen.blit(emp, (50, 573))
    screen.blit(red, (60, 574))

running = True
while running:
    
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                xchange = -1
            if event.key==pygame.K_d:
                xchange = 1
            if event.key==pygame.K_w:
                ychange = -1
            if event.key==pygame.K_s:
                ychange = 1
            if event.key==pygame.K_x:
                if lase["ready"]==1:
                    lase["on"]=1
        if event.type==pygame.KEYUP:
            xchange = 0
            ychange = 0


    playerx = playerx + xchange
    playery = playery + ychange

    if playerx > 736:
        playerx = 736
    if playerx < 0:
        playerx = 0
    if playery > 536:
        playery = 536
    if playery < 200:
        playery = 200
    player(playerx, playery)
    if lase["on"]==1:
        laser(playerx, playery, glaser)
        if lase["count"]==2500:
            lase["on"]=0
            lase["count"]=0
        else:
            lase["count"]+=1
    enemy(ship, jeff)
    healthbars(health, redhealth, bluehealth)
    ult(empty, redhealth, score)
    pygame.display.update()