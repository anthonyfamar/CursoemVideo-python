#Faça um programa em python que abra e reproduza o audio de um arquivo MP3.
import pygame

pygame.init()
pygame.mixer_music.load('D:\IMPORTANTE\Músicas\Drake - Toosie Slide.mp3')
pygame.mixer_music.play()
input()
pygame.event.wait()