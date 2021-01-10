import Variables
from Game_window import *
from Pole_generate_algorithm import *
from Setting_window import *
from Setting_befor_game_window import *
from Setting_in_game import *
from Main_window import *
import pygame
from Music import *

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        return '0'
    image = pygame.image.load(fullname)
    return image


def main():
    Variables.CHLVL = 0
    pygame.init()
    pygame.display.set_caption('Labyrinth')
    Variables.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    Variables.SCREEN_SIZE = Variables.SCREEN_HEIGHT, Variables.SCREEN_WIDTH = [Variables.screen.get_height(),
                                                                               Variables.screen.get_width()]
    gate_left = load_image('Gate_left.png')
    gate_left = pygame.transform.scale(gate_left, (Variables.SCREEN_WIDTH // 2, Variables.SCREEN_HEIGHT))
    gate_reight = load_image('Gate_reight.png')
    gate_reight = pygame.transform.scale(gate_reight, (int((Variables.SCREEN_WIDTH // 2 + 1) / (gate_reight.get_width() - 310) * gate_reight.get_width()), Variables.SCREEN_HEIGHT))
    gate_standart_pos = [-gate_reight.get_width() - 5, 0, Variables.SCREEN_WIDTH + 1, Variables.SCREEN_WIDTH - gate_reight.get_width() - 4]
    gate_pos = [-gate_reight.get_width() - 5, Variables.SCREEN_WIDTH + 1]
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    '''Я предлагаю основной цикл реализовать в этом файле, а при обновлении приложения вызывать соответствующие 
    методы из каждого класса'''
    Variables.window = MainWindow()
    running = True
    '''Чтобы реализовать полиморфизм и при этом не делать лишних перерисовок, окно настроек и полная отрисовка игрового
    поля будет в этом методе, а частичное обновление игрового поля будет в методе update()'''
    Variables.window.first_update()
    while running:
        if Variables.GATES_MOVI == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                '''Реализовать методы в классах, которые будут вызываться при различных событиях'''

                if event.type == pygame.KEYDOWN:
                    Variables.window.window_event(event.key)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pass
                        #event.pos
        if Variables.CHANGE_WINDOW:
            Variables.GATES_MOVI = 1
            Variables.FPS = 100
        if Variables.GATES_MOVI == 1:
            if gate_pos[0] + 20 >= gate_standart_pos[1]:
                gate_pos[0] += 5
                gate_pos[1] -= 5
            else:
                gate_pos[0] += 20
                gate_pos[1] -= 20
            if gate_pos[0] >= gate_standart_pos[1]:
                gate_pos[0] = gate_standart_pos[1]
                gate_pos[1] = gate_standart_pos[3]
                change_window()
                Variables.CHANGE_WINDOW = False
                var.screen.blit(gate_left, (gate_pos[0], 0))
                var.screen.blit(gate_reight, (gate_pos[1], 0))
                pygame.display.flip()
                pygame.time.delay(1000)
                Variables.GATES_MOVI = -1
        elif Variables.GATES_MOVI == -1:
            gate_pos[0] -= 20
            gate_pos[1] += 20
            if gate_pos[0] <= gate_standart_pos[0]:
                gate_pos[0] = gate_standart_pos[0]
                gate_pos[1] = gate_standart_pos[2]
                Variables.GATES_MOVI = 0
                Variables.FPS = 60
        if Variables.GATES_MOVI != 1:
            Variables.window.update()
        var.screen.blit(gate_left, (gate_pos[0], 0))
        var.screen.blit(gate_reight, (gate_pos[1], 0))
        pygame.display.flip()
        clock.tick(Variables.FPS)
    pygame.quit()


def change_window():
    if Variables.name == 'Главное меню':
        Variables.window = MainWindow()
    elif Variables.name == 'Настройки':
        Variables.window = Setting()
    elif Variables.name == 'Предыгровое меню':
        Variables.window = Pre_game_setting()
    elif Variables.name == 'Игровое меню':
        Variables.window = Pre_game_setting()
    elif Variables.name == 'Игра':
        Variables.window = Pole(read_pole(var.FILENAME[var.CHLVL], 1), read_pole(var.FILENAME[var.CHLVL], 2))
    Variables.window.first_update()


if __name__ == '__main__':
    main()
