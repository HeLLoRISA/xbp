import os
from pkgutil import extend_path
from tkinter import EXTENDED
import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
screen.fill((150,150,150))
pygame.display.set_caption('Invaders Game')

#画像を読み込む


running = True
while running:
    font = pygame.font.SysFont(None,80)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update() #スクリーン上の色を書き換えた
