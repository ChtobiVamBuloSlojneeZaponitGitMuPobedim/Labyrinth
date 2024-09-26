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
FILENAME = ['pole/Pole1.txt', 'pole/Pole2.txt', 'pole/Pole3.txt', 'pole/Pole4.txt', 'pole/Pole5.txt',
            'pole/Pole6.txt', 'pole/Pole7.txt', 'pole/Pole8.txt', 'pole/Pole9.txt', 'pole/Pole10.txt']
WAHACAL = [[4, 4, 2, 1], [6, 6, 2, 2], [8, 8, 2, 2], [10, 10, 2, 2], [16, 16, 2, 2],
         [8, 8, 3, 1], [10, 10, 3, 2], [12, 12, 3, 2], [10, 10, 4, 1], [12, 12, 4, 2]]
CHLVL = 0
CON = sqlite3.connect('data_base.db')
CUR = CON.cursor()
COLOR_ACTIVE = pygame.Color(41, 150, 150)
COLOR_INACTIVE = pygame.Color(9, 190, 150)
pygame.init()
FONT = pygame.font.Font(None, 32)
name = 'Главное меню'
CHANGE_WINDOW = False
GATES_MOVI = 0 # -1 - открытие ворот, 0 - стоят, 1 - закрытие ворот
