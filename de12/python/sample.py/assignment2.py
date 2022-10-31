from email import message
import os
from pkgutil import extend_path
from tkinter import EXTENDED, Y
import pygame
from pygame import mixer
from sqlalchemy import false #ミキサーをインポート
import random
import math
pygame.init()

screen = pygame.display.set_mode((800,600))
#screen.fill((150,150,150))
pygame.display.set_caption('Invaders Game')

# Player
playerimg = pygame.image.load('player.png')
playerX , playerY= 370, 480     #座標を変数に入れた
playerX_change = 0     #playerの位置

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change, enemyY_change = 4, 40

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX, bulletY = 0, 480 #Xはプレイヤーと同じ位置
bulletX_change, bulletY_change = 0, 3
bullet_state = 'ready'

# Score
score_value = 0

def player(x,y):
    screen.blit(playerimg,(x, y))

def enemy(x,y):
    screen.blit(enemyImg,(x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10)) #玉を表示

def isCollision(enemyX, enemyY, bulletX, bulletY): #玉とぶつかったかどうか
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False
    

running = True
while running:
    screen.fill((0,0,0))  
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -1
                if event.key == pygame.K_RIGHT:
                    playerX_change = 1 
                if event.key == pygame.K_SPACE:
                     if bullet_state is 'ready':
                          bulletX = playerX #プレイヤーの場所
                          fire_bullet(bulletX, bulletY) #表示

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                     playerX_change = 0
    # Player
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736 #プレイヤーの制限

    # Enemy
    if enemyY > 440:
        break #敵が画面下まできたらブレイク
    enemyX += enemyX_change
    if enemyX <= 0: #左端に来たら
        enemyX_change = 0.3 #プラスされる
        enemyY += enemyY_change #下に移している
    elif enemyX >=736: #右端に来たら
        enemyX_change = -0.3 #マイナスされる
        enemyY += enemyY_change

    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision: #衝突した場合
        bulletY = 480
        bullet_state = 'ready'
        score_value += 1
        enemyX = random.randint(0, 736) #新たな敵の出現
        enemyY = random.randint(50, 150)
     
    # Bullet Movement
    if bulletY <=0: #玉が当たらなかった場合
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY) #玉を表示
        bulletY -= bulletY_change  #値をマイナスにしている

    # Score
    font = pygame.font.SysFont(None, 32) # フォントの作成　Noneはデフォルトのfreesansbold.ttf
    score = font.render(f"Score : {str(score_value)}", True, (255,255,255)) # テキストを描画したSurfaceの作成
    screen.blit(score, (20,50))




    player(playerX, playerY)
    enemy(enemyX, enemyY)
  
    pygame.display.update() #書き換え
