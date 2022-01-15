import os
import time
import random
import pygame
import keyboard

# Loading song names
songs = os.listdir('./songs')

def print_controls():
    """
    Print Controls on the screen.
    """
    print('p: Pause\nu: Unpause/Resume\nspace: Play Next\nESC: Stop')

# Initialization of modules
pygame.init()
pygame.mixer.init()

while True:
    # Playing random song from the list
    song = random.choice(songs)
    pygame.mixer.music.load('./songs/' + song)
    pygame.mixer.music.play()

    os.system('cls');
    print('Now Playing: ' + song)
    print_controls()

    # Wait till the song is playing and listen for input keys
    while pygame.mixer.music.get_busy():
        key = keyboard.read_key()

        if key == 'p':
            pygame.mixer.music.pause()
            print('Paused')

            while True:
                if keyboard.is_pressed('u'):
                    pygame.mixer.music.unpause()

                    os.system('cls');
                    print('Now Playing: ' + song)
                    print_controls()

                    break
        if key == 'space':
            pygame.mixer.music.stop()
            break
        if key == 'esc':
            exit()