import sqlite3
import pygame

FONT_SIZE = 18
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
FPS = 60
WIN = False
POLE_SIZE = [[7, 5], [14, 10], [21, 15]]
COLOR_VALUE = {
    'r': 'red',
    'b': 'blue',
    'g': 'green',
    'y': 'yellow',
    'o': 'orange'
}
FILENAME = ['pole/Pole1.txt', 'pole/Pole2.txt', 'pole/Pole3.txt', 'pole/Pole4.txt']
CHLVL = 1
CON = sqlite3.connect('data_base.db')
CUR = CON.cursor()
COLOR_ACTIVE = pygame.Color(41, 150, 150)
COLOR_INACTIVE = pygame.Color(9, 190, 150)
pygame.init()
FONT = pygame.font.Font(None, 32)
name = 'Главное меню'
CHANGE_WINDOW = False
GATES_MOVI = 0 # -1 - открытие ворот, 0 - стоят, 1 - закрытие ворот
