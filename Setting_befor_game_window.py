from Window import Pra_window
import pygame
import Variables as var
from Music import *


def print_text(message, x, y, font_color=(0, 0, 0), font_type='Marta_Decor_Two.ttf', font_size=20):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    var.screen.blit(text, (x, y))


class Pre_game_setting(Pra_window):
    def __init__(self):
        super().__init__()

    def first_update(self):
        self.input_box1 = InputBox(10, 10, 140, 32)
        self.input_box2 = InputBox(10, 52, 140, 32)
        self.input_boxes = [self.input_box1, self.input_box2]
        self.button = Button(80, 40)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
            for box in self.input_boxes:
                box.handle_event(event)
        for box in self.input_boxes:
            box.update()
        var.screen.fill((30, 30, 30))
        for box in self.input_boxes:
            box.draw(var.screen)
        self.button.draw(10, 100, 'Назад в меню')
        print_text('Размер лабиринта', 240, 10, (60, 140, 190), font_size=30)
        print_text('Количество цветов дверей', 240, 52, (60, 140, 190), font_size=30)


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = var.COLOR_INACTIVE
        self.text = text
        self.txt_surface = var.FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = var.COLOR_ACTIVE if self.active else var.COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = var.FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (41, 150, 150)
        self.active_color = (9, 190, 150)

    def draw(self, x, y, text, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(var.screen, self.inactive_color, (x, y, self.width, self.height))
                if click[0] == 1:
                    pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(150)
                    # Смена окна
                    if text == 'Назад в меню':
                        var.name = 'Главное меню'
                        var.CHANGE_WINDOW = True
            else:
                pygame.draw.rect(var.screen, self.active_color, (x, y, self.width, self.height))
        else:
            pygame.draw.rect(var.screen, self.active_color, (x, y, self.width, self.height))
        print_text(text, x + 5, y + 5)