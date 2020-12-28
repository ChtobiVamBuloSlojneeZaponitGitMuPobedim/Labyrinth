from Window import Pra_window
import Variables as var
import pygame


class Main_menu(Pra_window):
    def __init__(self):
        super().__init__()

    def first_update(self):
        pygame.draw.line(var.screen, (255, 0, 0), (0, 0), (100, 40))