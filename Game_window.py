from Window import Pra_window
import Variables as var
import Pole_generate_algorithm as pga
import pygame
import sys
import os
import math


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        return '0'
    image = pygame.image.load(fullname)
    return image


class Pole(Pra_window):
    # size - размеры игрового поля (в клетках)
    def __init__(self, size, colors):
        super().__init__()
        self.width = size[0]
        self.height = size[1]
        self.cell_size = int(min([var.SCREEN_WIDTH, var.SCREEN_HEIGHT * 0.9]) // max(size))
        self.board = pga.generate_pole(size, colors)
        self.left = (var.SCREEN_WIDTH - self.cell_size * self.width) // 2
        self.top = var.SCREEN_HEIGHT * 0.1



    def first_update(self):
        var.screen.fill('black')
        self.all_sprites = pygame.sprite.Group()
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                name = ''
                for k in self.board[i][j]:
                    if k != 's':
                        name += '1'
                    else:
                        name += '0'
                alpha = 0
                im = load_image(name + ".png")
                while im == '0':
                    name = name[1:] + name[0]
                    im = load_image(name + ".png")
                    alpha -= 90
                cell = pygame.sprite.Sprite(self.all_sprites)
                cell.image = pygame.transform.scale(im, (self.cell_size, self.cell_size))
                cell.rect = im.get_rect()
                cell.rect.x = int(self.left + self.cell_size * j)
                cell.rect.y = int(self.top + self.cell_size * i)
                print(i, j, alpha)
                center = (int(self.left + self.cell_size * j) + self.cell_size // 2,
                          int(self.top + self.cell_size * i) + self.cell_size // 2)
                cell.image = pygame.transform.rotate(cell.image, alpha)
        self.all_sprites.draw(var.screen)

    def update(self):
        pass