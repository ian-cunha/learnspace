# Faça um programa em Python que abra e reproduza o
# aúdio de um arquivo MP3.

import pygame
import os
print(os.getcwd)
pygame.init()
pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), 'ex021.mp3'))
pygame.mixer.music.play()
pygame.event.wait()