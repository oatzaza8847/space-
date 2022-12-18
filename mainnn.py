import pygame
import math
import random

pygame.init()


WIDTH = 1000
HEIGHT = 800 

#################### window ############################################

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('KHAWOAT!!!')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon) 
BG = pygame.image.load('BG.jpg')  

#################### player ##########################################

psize = 128
pimg = pygame.image.load("space.png")
px = 100
py = HEIGHT - psize
pxchange = 0

def Player (x,y):
    screen.blit(pimg,(x,y))
    #blit = ภาพที่เราวางไว้หน้าจอ

#################### Enemy ############################################

esize = 64
eimg = pygame.image.load("aline.png")
ex = 50
ey = 0
#eychange =1

def enemy(x,y):
    screen.blit(eimg,(x,y))

#################### multi-Enemy ####################################
exlist = [] #ตน แกนx
eylist = [] #ตน แกนy
ey_change_list = [] # ความเร็ว enemy
allenemy = 3

for i in range(allenemy):
    exlist.append(random.randint(0,WIDTH - esize))
    eylist.append(random.randint(0,100))
    #ey_change_list.append(random.randint(1,5))
    ey_change_list.append(1)#


#################### aster ##########################################

asize = 64
aimg = pygame.image.load("aster.png")
ax = 50
ay = 0
#eychange =1

def aster(x,y):
    screen.blit(aimg,(x,y))

#################### multi- aster ##################################
axlist = [] #ตน แกนx
aylist = [] #ตน แกนy
ay_change_list = [] # ความเร็ว enemy
allaster = 3

for i in range(allaster):
    axlist.append(random.randint(0,WIDTH - asize))
    aylist.append(random.randint(0,100))
    #ey_change_list.append(random.randint(1,5))
    ay_change_list.append(1)


################### sss #########################################

ssize = 64
simg = pygame.image.load('sss.png')
sx = 50
sy = 0
allsss = 1

def sss (x,y):
    screen.blit(simg,(x,y))
'''
def sssisCollision (scx,scy,pcx,pcy):
    #เช็คว่าชนมั้ยถ้าชนจะ true
    sssdistance = math.sqrt(math.pow(scx - pcx ,2)+math.pow(scy - pcy,2))
    print(sssdistance)
    if sssdistance < (ssize / 2) + (psize / 2):
        return True
    else:
        return False
'''

################### Star ######################################## ^^^

msize =32
mimg = pygame.image.load('star.png')
mx = 100
my = HEIGHT - psize
mychange = 50
mstate = 'ready'

def fire_star(x,y):
    global mstate
    mstate = 'fire'
    screen.blit(mimg,(x,y))

def isCollision(wcx,wcy,rcx,rcy):
    #เช็คว่าชนมั้ยถ้าชนจะ true
    distance = math.sqrt(math.pow(wcx - rcx ,2)+math.pow(wcy - rcy,2))
    print(distance)
    if distance < (esize / 2) + (msize / 2):
        return True
    else:
        return False





#################### Score ###########################################

allscore = 0
font = pygame.font.Font('Avenir Next Condensed.ttc',30)

def showscore():
    score = font.render('POINT : {} POINT'.format(allscore),True,(255,255,255))
    screen.blit(score,(30,30))

#################### sound ############################################

pygame.mixer.music.load('658450__matrixxx__hallucinations-in-brooklyn-city-trap.wav')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

################### game over #######################################
fontover = pygame.font.Font('Avenir Next Condensed.ttc',100)
fontover2 = pygame.font.Font('Avenir Next Condensed.ttc',30)

playsound = False
gameover = False
def GameOver():

    global playsound
    global gameover
    overtext = fontover.render('GAME OVER',True,(255,255,255))
    screen.blit(overtext,(270,300))
    overtext2 = fontover2.render('PRESS [N] NEW GAME',True,(255,255,255))
    screen.blit(overtext2,(390,420))
    if playsound == False:
        sound = pygame.mixer.Sound('Over.wav')
        sound.play()
        playsound = True
    #if gameover == False:
     #   gameover = True







#################### game loop #######################################

runnig = True

clock = pygame.time.Clock()
FPS = 30

while runnig:
    
    screen.blit(BG,(0,0))
    for event in pygame.event.get():
        #หากrun loopเช็คว่ากดปิด pygame [x]
        if event.type == pygame.QUIT:
            runnig = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pxchange = -20

            if event.key == pygame.K_RIGHT:
                pxchange = 20

            if event.key == pygame.K_SPACE:
                if mstate == 'ready':
                    mx = px + 50 #ขยับไปตรงกลาง
                    fire_star(mx,my)
                    sound = pygame.mixer.Sound('laser.wav')
                    sound.play()

            if event.key == pygame.K_n:
                #gameover = False
                playsound = False
                allscore = 0
                for i in range(allenemy):
                    eylist[i] = random.randint(0,100)
                    exlist[i] = random.randint(0,WIDTH - esize)
                    ey_change_list[i] = 1

                    aylist[i] = random.randint(0,100)
                    axlist[i] = random.randint(0,WIDTH - asize)
                    ay_change_list[i] = 1

                    sy = random.randint(0,100)
                    sx = random.randint(0,WIDTH - esize)
                    sy_change = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pxchange = 0

################### run player ##############################################

    #px,py is start point 
    Player (px,py-10)

    if px <= 0 :
    ### ชนขวา ปรับ ค่าเป็นลบ ####
        px = 0
        px += pxchange

    elif px >= WIDTH - psize:
    ### ชนซ้าย ปรับ ค่าเป็นลบ ####
        px = WIDTH - psize
        px += pxchange

    ### นอกนั้นให้ px ปรับค่าตาม pxchange ###
    else:
        px +=pxchange
    '''
    ###### do player ขยับซ้ายขวาเมื่อชนขอบจอ #######
    if px <= 0 :
    ### ชนขวา ปรับ ค่าเป็นลบ ####
        pxchange = 5
        px += pxchange

    elif px >= WIDTH - psize:
    ### ชนซ้าย ปรับ ค่าเป็นลบ ####
        pxchange = -5
        px += pxchange

    ### นอกนั้นให้ px ปรับค่าตาม pxchange ###
    else:
    '''
####run enemy ตัวแรกที่ทดลอง #####
    
   # enemy(ex ,ey)
    #ey += eychange

################### run multi-enemy  #########################################
    

    for i in range(allsss):
                if sy > HEIGHT + (ssize * 5) and gameover == False:
                    for i in range(allsss):
                        sy = random.randint(0,100)
                        sx = random.randint(0,WIDTH - esize)
                        sy = sychane

    for i in range(allenemy):
        if eylist[i] > HEIGHT - esize and gameover == False:
            for i in range(allenemy):
                aylist[i] = 1000
                eylist[i] = 1000
                sy = 1000
            GameOver()
            break

    for i in range(allaster):             
        if aylist[i] > HEIGHT - asize and gameover == False:
            for i in range(allaster):
                aylist[i] = 1000
                eylist[i] = 1000
                sy = 1000
            GameOver()
            break

        if GameOver == True:
            overtext = fontover.render('GAME OVER',True,(255,255,255))
            screen.blit(overtext,(300,400))

        #เพิ่มความเร็วของ enemy
        eylist[i] += ey_change_list[i]
        collisionmulit = isCollision(exlist[i],eylist[i],mx,my)
        if collisionmulit:
            my = HEIGHT - psize
            matate = 'ready'
            eylist[i] = 0 
            exlist[i] = random.randint(0,HEIGHT - esize)
            allscore += 1
            ey_change_list[i] += 1
            sound = pygame.mixer.Sound('explosion.wav')
            sound.play()
        enemy(exlist[i],eylist[i])

################### run multi-aster  ##########################################
        
        #เพิ่มความเร็วของ enemy
        aylist[i] += ay_change_list[i]
        khawoat = isCollision(axlist[i],aylist[i],mx,my)
        if khawoat:
            my = HEIGHT - psize
            matate = 'ready'
            aylist[i] = 0 
            axlist[i] = random.randint(0,HEIGHT - asize)
            allscore += 10
            ay_change_list[i] += 1
            sound = pygame.mixer.Sound('explosion.wav')
            sound.play()
        aster(axlist[i],aylist[i])
        
################### run star  ################################################

    if mstate == 'fire' :
        fire_star(mx,my)
        my -= mychange

        #เช็คกระสุนไปชนจอยัง ถ้าชนให้ state "ready"
    if my <= 0:
        my = HEIGHT - psize 
        mstate = 'ready'

        #เช็คว่าชนกันหรือไม่?
    collision = isCollision(ex,ey,mx,my)
    if collision:
        my = HEIGHT - psize
        mstate = 'ready'
        ey = 0
        ex = random.randint(0,WIDTH - esize) #สุ่ม ตน ของศัตรู
        allscore += 1
        sound = pygame.mixer.Sound('explosion.wav')
        sound.play()

    khawoat  = isCollision(ax,ay,mx,my)
    if khawoat:
        my = HEIGHT - psize
        mstate = 'ready'
        ay = 0
        ax = random.randint(0,WIDTH - asize) #สุ่ม ตน ของศัตรู
        allscore += 1
        sound = pygame.mixer.Sound('explosion.wav')
        sound.play()
    

################## run sss  ####################################################  


    sss (sx,sy)
    for i in range(allsss):
        if sy >= 0:
            sychane = 2
            sy += sychane
        
        ssscollision = isCollision(sx,sy,px,py)
        if ssscollision:
            sy = HEIGHT - psize
            sy = 0
            sx = random.randint(0,WIDTH - ssize) #สุ่ม ตน ของศัตรู∫
            sound = pygame.mixer.Sound('explosion.wav')
            sound.play()
        

        if ssscollision:
            for i in range(allaster):  
                aylist[i] = 0 
                axlist[i] = random.randint(0,WIDTH - asize)
                ay_change_list[i] = 1
                aylist[i] += ay_change_list[i]
                sound = pygame.mixer.Sound('explosion.wav')
                sound.play()
            aster(axlist[i],aylist[i])

        
        if ssscollision:
            for i in range(allenemy):
                eylist[i] = 0 
                exlist[i] = random.randint(0,WIDTH - esize)
                ey_change_list[i] = 1
                eylist[i] += ey_change_list[i]
                sound = pygame.mixer.Sound('explosion.wav')
                sound.play()
            enemy(exlist[i],eylist[i])
        

    ################################################################################

    showscore()
    print(px)
    pygame.display.update()
    pygame.display.flip()
    pygame.event.pump()
    screen.fill((0,0,0))
    clock.tick(FPS)




