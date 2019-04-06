import time
import pygame
pygame.init()
pygame.mixer.init()

word = "at"

if word[0] == "a" and word[1] == "t":
    pygame.mixer_music.load("./A.mp3")
    pygame.mixer.music.play(1)
    pygame.mixer_music.load("./T.mp3")
    pygame.mixer.music.play(1)

pygame.event.wait()