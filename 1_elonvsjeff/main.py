import pygame

pygame.init()

icon = pygame.image.load("./assets/icon.png")
playerimg = pygame.image.load("./assets/elon.png")
desmond = pygame.image.load("./assets/desboss.png")
glaser = pygame.image.load("./assets/laser.png")
jeff = pygame.image.load("./assets/jeff.png")
ship = pygame.image.load("./assets/ship.png")
empty = pygame.image.load("./assets/emptybar.png")
redhealth = pygame.image.load("./assets/redbar.png")
bluehealth = pygame.image.load("./assets/bluebar.png")
bitcoin = pygame.image.load("./assets/bitcoin.png")
lasedjeff = pygame.image.load("./assets/lasedjeff.png")

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Elon vs Jeff")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
playerx = 370
playery = 480
state = 0
xchange = 0
ychange = 0
abilities = [1, 0, 0]  #score for ult, bool for gatling, bool for regen
coins = []
coincount = 0
health = {"elon":1001, "jeff":5001}
lase = {"ready":0, "on":0, "count":0}

def player(img, x, y):
    screen.blit(img, (x, y))

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

def shoot(health, coincount, coins, time = 300):
    if coincount==time:
        x = playerx+16
        y = playery-32
        coins.append([x, y])
        coincount = 0
    coincount+=1
    removelist = []
    for i in range(len(coins)):
        if coins[i][1]>100:
            screen.blit(bitcoin, (coins[i][0], coins[i][1]))
            coins[i]=[coins[i][0], coins[i][1]-1]
        else:
            removelist.append(i)
            if health["jeff"]>0:
                health["jeff"] -= 20
                if abilities[0]<30:
                    abilities[0]+=1
    coinlist = []
    for i in range(len(coins)):
        if i not in removelist:
            coinlist.append(coins[i])
    coins = coinlist
    del coinlist
    return [health, coincount, coins]


running = True
gatlingcount = 0
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


    if abilities[0]==30:
        lase["ready"]=1
    playerx = playerx + xchange
    playery = playery + ychange

    if playerx > 736:
        state = 0
        playerx = 736
    if playerx < 0:
        state = 1
        playerx = 0
    if playery > 536:
        playery = 536
    if playery < 200:
        playery = 200
    if state ==0:
        player(playerimg, playerx, playery)
    else:
        player(desmond, playerx, playery)
    if lase["on"]==1:
        laser(playerx, playery, glaser)
        if lase["count"]==2000:
            lase["on"]=0
            lase["count"]=0
            lase["ready"]=0
            abilities[0]=1
        else:
            lase["count"]+=1
            health["jeff"]-=0.5
    if lase["on"]!=1:
        enemy(ship, jeff)
        if abilities[1]==1:
            if gatlingcount==40:
                abilities[1]=0
            else:
                [health, coincount, coins] = shoot(health, coincount, coins, time =50)
                gatlingcount+=1
        else:
            [health, coincount, coins] = shoot(health, coincount, coins)
        [health, coincount, coins] = shoot(health, coincount, coins)
    else:
        enemy(ship, lasedjeff)
    healthbars(health, redhealth, bluehealth)
    ult(empty, redhealth, abilities[0])
    pygame.display.update()