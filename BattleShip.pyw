import pygame
import random
import math
pygame.init()
running = True
gameOver=False
score=0
font= pygame.font.Font("Data/Bubblegum.ttf",32)
credit=pygame.font.Font("freesansbold.ttf",16)
credit_val=credit.render("Dev: Rajeswar",True,(255,255,255))
gameOver_font=pygame.font.Font("Data/Bubblegum.ttf",100)
textX=10
textY=10
Screen= pygame.display.set_mode((800,600))
pygame.display.set_caption("Battle Ship Worrior")
icon = pygame.image.load("Data/icon.png")

#enemy spaceship
spaceship=pygame.image.load("Data/spaceship.png")
pygame.display.set_icon(icon)
bullet=pygame.image.load("Data/bullets.png")
def Display_score(X,Y):
    score_val=font.render("Score : "+str(score),True,(109,192,227))
    Screen.blit(score_val,(X,Y))
    global credit_val
    Screen.blit(credit_val,(660,580))
#gameOver Display_score
def Display_GameOver():
    gameOver_text=gameOver_font.render("GAME OVER...!",True,(255,0,0))
    finalscore=gameOver_font.render("SCORE: "+str(score),True,(255,255,255))
    space=credit.render("Press space to reset",True,(255,255,255))
    Screen.blit(gameOver_text,(100,250))
    Screen.blit(finalscore,(170,350))
    Screen.blit(space,(300,500))

#player attributes
playerX=370
playerY=495
rateX=0
rateY=0
#Enemy attributes
no_of_enemy=9
enemy=list()
enemyX=list()
enemyY=list()
rate_enemyX=list()
rate_enemyY=list()
for i in range(no_of_enemy):
    enemy.append(pygame.image.load("Data/enemy2.png"))
    enemyX.append(random.randint(0,768))
    enemyY.append(random.randint(0,100))
    rate_enemyX.append(2)
    rate_enemyY.append(30)
#Bullet attributes
bulletX=0
bulletY=0
bullet_rateY=6
bullet_state="ready"

def readyBullet(X,Y):
    global bulletX
    global bulletY
    bulletX=X
    bulletY=Y

def fireBullet(X,Y):
    global bullet_state
    bullet_state="fire"
    Screen.blit(bullet,(X+16,Y+10))

def player(X,Y):
    Screen.blit(spaceship,(X,Y))

def Enemy(X,Y,i):
    Screen.blit(enemy[i],(X,Y))

def isCollide(Xenemy,Yenemy,Xbullet,Ybullet):
    dist = math.sqrt( (Xenemy-Xbullet)**2 + (Yenemy-Ybullet)**2 )
    if dist<=32: return True
    return False


while running:
    Screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#Player Movement
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                rateX=-2
            if event.key==pygame.K_RIGHT:
                rateX=2
            if event.key==pygame.K_UP:
                rateY=-2
            if event.key==pygame.K_DOWN:
                rateY=2
            if event.key==pygame.K_SPACE:
                fireBullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                rateX=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                rateY=0
#player movement boundings
    if(playerX+rateX<=736 and playerX+rateX>= 0):playerX+=rateX
    if(playerY+rateY>=0 and playerY+rateY<=536): playerY+=rateY
#enemy movement
    for i in range(no_of_enemy) :
        if gameOver==True: break
        if(enemyX[i]+rate_enemyX[i] > 768 or enemyX[i]+rate_enemyX[i]<0):
             rate_enemyX[i]=-rate_enemyX[i]
             enemyY[i]+=rate_enemyY[i]
        enemyX[i]+=rate_enemyX[i]
        if enemyY[i]>=586:
            enemyX[i]=random.randint(0,768)
            enemyY[i]=random.randint(0,100)
#collision
        if isCollide(enemyX[i],enemyY[i],bulletX,bulletY) and bullet_state=="fire":
            print("Killed")
            bullet_state="ready"
            score+=5
            enemyX[i]=random.randint(0,768)
            enemyY[i]=random.randint(0,100)
#update enemy postion
        Enemy(enemyX[i],enemyY[i],i)
        if isCollide(enemyX[i],enemyY[i],playerX,playerY):
            print("player Dead")
            gameOver=True
            break
#gameOver
    if gameOver:
        Display_GameOver()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    score=0
                    print("reset mode")
                    gameOver=False
                    playerX= 370
                    playerY= 495
                    rateX=0
                    rateY=0
                    player(playerX,playerY)
                    for i in range(no_of_enemy):
                        enemyX[i]=random.randint(0,768)
                        enemyY[i]=random.randint(0,100)
                        rate_enemyX[i]=2
                        rate_enemyY[i]=30
                        Enemy(enemyX[i],enemyY[i],i)
        continue
#update player postion
    player(playerX,playerY)
#bullet update
    if bullet_state=="fire":
        fireBullet(bulletX,bulletY)
        bulletY-=bullet_rateY
        if bulletY<=0: bullet_state="ready"
    else:
        readyBullet(playerX,playerY)
    Display_score(textX,textY)

    pygame.display.update()
