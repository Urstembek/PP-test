import pygame
import sys
from pygame.locals import *


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((750, 500))
background = pygame.image.load('background.png')

tracks = ['song1.mp3', 'song2.mp3']
current_track = 0
paused = False

def play_music():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.load(tracks[current_track])
        pygame.mixer.music.play()
        paused = False

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(tracks)
    play_music()

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(tracks)
    play_music()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_p:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                else:
                    play_music()
            elif event.key == K_s:
                stop_music()
            elif event.key == K_n:
                next_track()
            elif event.key == K_b:
                prev_track()

    screen.blit(background, (0, 0))
    pygame.display.update()