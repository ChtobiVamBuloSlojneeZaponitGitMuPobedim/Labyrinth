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
        self.left = (var.SCREEN_WIDTH - self.cell_size * (self.width + 1)) // 2
        print(self.left)
        self.top = var.SCREEN_HEIGHT * 0.1



    def first_update(self):
        var.screen.fill('black')
        self.all_cells_sprites = pygame.sprite.Group()
        self.all_doors = pygame.sprite.Group()
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
                cell = pygame.sprite.Sprite(self.all_cells_sprites)
                cell.image = pygame.transform.scale(im, (self.cell_size, self.cell_size))
                cell.rect = im.get_rect()
                cell.rect.x = int(self.left + self.cell_size * j)
                cell.rect.y = int(self.top + self.cell_size * i)
                cell.image = pygame.transform.rotate(cell.image, alpha)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                for k in range(len(self.board[i][j])):
                    dor = self.board[i][j][k]
                    if dor == 's' or dor == 'n':
                        continue
                    if k == 3:
                        alpha = -90
                    if k == 0:
                        alpha = 0
                    if k == 2:
                       alpha = 0
                    if k == 1:
                        alpha = -90
                    if k < 2:
                        dor += '1'
                    else:
                        dor += '2'
                    im = load_image(dor + ".png")
                    cell = pygame.sprite.Sprite(self.all_doors)
                    im_height = self.cell_size // 5
                    im_width = self.cell_size // 12
                    cell.image = pygame.transform.scale(im, (im_height, im_width))
                    cell.rect = im.get_rect()
                    if k == 0:
                        cell.rect.x = int(self.left + self.cell_size * j + self.cell_size / 5 * 2)
                        cell.rect.y = int(self.top + self.cell_size * i)
                    elif k == 1:
                        cell.rect.x = int(self.left + self.cell_size * (j + 1) - im_width)
                        cell.rect.y = int(self.top + self.cell_size * i + self.cell_size / 5 * 2)
                    elif k == 2:
                        cell.rect.x = int(self.left + self.cell_size * j + self.cell_size / 5 * 2)
                        cell.rect.y = int(self.top + self.cell_size * (i + 1) - im_width)
                    else:
                        cell.rect.x = int(self.left + self.cell_size * j)
                        cell.rect.y = int(self.top + self.cell_size * i + self.cell_size / 5 * 2)
                    cell.image = pygame.transform.rotate(cell.image, alpha)

        self.all_cells_sprites.draw(var.screen)
        self.all_doors.draw(var.screen)

    def update(self):
        pass