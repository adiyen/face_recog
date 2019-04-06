import time
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer_music.load("./test2.mp3")
pygame.mixer.music.play(2)

pygame.event.wait()