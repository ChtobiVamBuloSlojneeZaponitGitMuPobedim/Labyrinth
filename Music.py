import pygame
import keyboard


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.music.load('data\\579b2fbcdd508f7.mp3')
pygame.mixer.music.set_volume(0.2)
button_sound = pygame.mixer.Sound('data\\00171.wav')
pygame.mixer.Sound.set_volume(button_sound, 0.2)
Flag = True


def Hot_key():
    global Flag
    if Flag == True:
        pygame.mixer.music.pause()
        Flag = False
    else:
        pygame.mixer.music.unpause()
        Flag = True


keyboard.add_hotkey('p', Hot_key)