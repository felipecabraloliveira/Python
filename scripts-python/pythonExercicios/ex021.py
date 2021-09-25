# Exercicio 021 do curso de Python - Curso em vídeo

# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# Meu código

import Play_mp3
Play_mp3.play(r'C:\Users\Felipe\Documents\PC-Trampo\Python\scripts-python\pythonExercicios\300.mp3')

# Correção - Utilizando o módulo pygame

import pygame
pygame.init()
pygame.mixer.music.load('300.mp3')
pygame.mixer.music.play()
pygame.event.wait()
