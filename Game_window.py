from Window import Pra_window
import Variables as var
from Setting_in_game import *
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
        self.cell_size = min([int((var.SCREEN_HEIGHT * 0.89) // self.height),
                              int(var.SCREEN_WIDTH // self.width)])
        self.board = pga.generate_pole(size, colors)
        self.left = (var.SCREEN_WIDTH - self.cell_size * self.width) // 2
        self.top = var.SCREEN_HEIGHT * 0.1

    def first_update(self):
        var.screen.fill('black')
        self.all_cells_sprites = pygame.sprite.Group()
        self.all_doors = pygame.sprite.Group()
        self.hero_sprites = pygame.sprite.Group()
        self.hero = Hero(self.width - 1, 0, self.hero_sprites, self.cell_size, self.left, self.top, [self.height, self.width])
        self.draw_cells()
        self.draw_doors()
        self.all_cells_sprites.draw(var.screen)
        self.all_doors.draw(var.screen)
        self.hero_sprites.draw(var.screen)

    def update(self):
        self.hero_sprites.update(-1)
        self.all_cells_sprites.draw(var.screen)
        self.all_doors.draw(var.screen)
        self.hero_sprites.draw(var.screen)

    def window_event(self, key_press):
        if key_press == pygame.K_LEFT:
            self.hero_sprites.update(3)
        if key_press == pygame.K_RIGHT:
            self.hero_sprites.update(1)
        if key_press == pygame.K_UP:
            self.hero_sprites.update(0)
        if key_press == pygame.K_DOWN:
            self.hero_sprites.update(2)
        if key_press == pygame.K_ESCAPE:
            # Переключение на экран настроек
            Variables.window = Set_in_game()

    def draw_cells(self):
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

    def draw_doors(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                for k in range(len(self.board[i][j])):
                    dor = self.board[i][j][k]
                    if dor == 's' or dor == 'n':
                        continue
                    if k == 3 or k == 1:
                        alpha = -90
                    if k == 0 or k == 2:
                        alpha = 0
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


class Hero(pygame.sprite.Sprite):
    image = load_image("hero.png")

    def __init__(self, x, y, group, height, left, top, size):
        super().__init__(group)
        self.image = pygame.transform.scale(Hero.image, (height // 5, height // 5))
        self.height = height
        self.left = left
        self.top = top
        self.rect = self.image.get_rect()
        self.rect.x = self.left + x * self.height + self.height // 5 * 2
        self.rect.y = self.top + y * self.height + self.height // 5 * 2
        self.travel = False
        self.proid_put = 0
        self.del_put = 15
        self.per_po = 'x'
        self.hero_way = [[y, x]]
        self.nazad = False
        self.size = size


    def update(self, napr):
        if self.travel:
            self.rect.y += (self.hero_way[-1][0] - self.hero_way[-2][0]) * self.height // self.del_put
            if self.proid_put + 1 == self.del_put:
                self.rect.y = self.top + self.hero_way[-1][0] * self.height + self.height // 5 * 2
            self.rect.x += (self.hero_way[-1][-1] - self.hero_way[-2][-1]) * self.height // self.del_put
            if self.proid_put + 1 == self.del_put:
                self.rect.x = self.left + self.hero_way[-1][-1] * self.height + self.height // 5 * 2
            self.proid_put += 1
            if self.proid_put == self.del_put:
                self.proid_put = 0
                self.travel = False
        elif napr == -1:
            return
        elif not self.travel:
            self.travel = True
            if napr % 2 == 0:
                if [self.hero_way[-1][0] + int(str(napr - 1)[:-1] + '1'), self.hero_way[-1][-1]] not in self.hero_way[: -2]:
                    if [self.hero_way[-1][0] + int(str(napr - 1)[:-1] + '1'), self.hero_way[-1][-1]] in self.hero_way:
                        self.nazad = True
                    else:
                        self.hero_way.append([self.hero_way[-1][0] + int(str(napr - 1)[:-1] + '1'), self.hero_way[-1][-1]])
                        self.nazad = False
                else:
                    self.travel = False
            else:
                if [self.hero_way[-1][0], self.hero_way[-1][-1] + int(str(-(napr - 2))[:-1] + '1')] not in self.hero_way[: -2]:
                    if [self.hero_way[-1][0], self.hero_way[-1][-1] + int(str(-(napr - 2))[:-1] + '1')] in self.hero_way:
                        self.nazad = True
                    else:
                        self.hero_way.append([self.hero_way[-1][0], self.hero_way[-1][-1] + int(str(-(napr - 2))[:-1] + '1')])
                        self.nazad = False
                else:
                    self.travel = False
            if (self.hero_way[-1][-1] >= self.size[-1] or self.hero_way[-1][0] >= self.size[0] or
                    self.hero_way[-1][-1] < 0 or self.hero_way[-1][0] < 0):
                self.travel = False
                del self.hero_way[-1]
                self.nazad = False
            print(self.hero_way)