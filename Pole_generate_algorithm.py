import Variables as var
import random

def read_pole(filename, flag):
    f = open(filename, 'r')
    g = f.readlines()
    a = []
    width = 0
    height = 0
    color = 1
    for i in range(1, len(g) - 1):
        b = g[i]
        for j in range(1, len(b) - 2):
            if g[i][j] == 'b' and color < 2:
                color = 2
            if g[i][j] == 'g' and color < 3:
                color = 3
            if g[i][j] == 'o' and color < 4:
                color = 4
            if g[i][j] == 't' and color < 5:
                color = 5            
    for i in range(1, len(g) - 1, 2):
        height += 1
        b = g[i]
        d = []
        width = 0
        for j in range(len(b)):
            c = []
            if b[j] == '0' or b[j] == '1' or b[j] == '2':
                width += 1
                c.append(g[i - 1][j])
                c.append(g[i][j + 1])
                c.append(g[i + 1][j])
                c.append(g[i][j - 1])
            if len(c) != 0:
                d.append(c)
        if len(d) != 0:
            a.append(d)
    if flag == 0:
        return a
    if flag == 1:
        return width, height
    if flag == 2:
        return color

def generate_random_pole(w, h, c, l): # width, height, col-vo colors, level(1, 2, 3)
    col = ['r', 'b', 'g', 'o', 't' 'y'] # red, blue, green, orange, light blue, yellow
    if c < 2:
        return 'Error'
    if w < 3:
        return 'Error'
    if h < 3:
        return 'Error'
    x = 0 #position hero x
    y = 0 #position hero y
    d = 0 #color door
    pole = []
    for i in range(h):
        a = []
        for j in range(w):
            b = []
            c1 = 'n' # c1 - вверх
            c2 = 'n' # c2 - вправо
            c3 = 'n' # c3 - вниз
            c4 = 'n' # c4 - влево
            if i == 0:
                c1 = 's'
            if j == 0:
                c4 = 's'
            if j == w - 1:
                c2 = 's'
            if i == h - 1:
                c3 = 's'
            b.append(c1)
            b.append(c2)
            b.append(c3)
            b.append(c4)
            a.append(b)
        pole.append(a)
    if l == 1:
        while x != w - 1 or y != h - 1:
            a = random.randint(1, 2) # 1 - Вниз, 2 - Влево
            if a == 1:
                if y != h - 1:
                    pole[y][w - x - 1][2] = col[d]
                    pole[y + 1][w - x - 1][0] = col[d]
                    d += 1
                    if d == c:
                        d = 0
                    y += 1
            if a == 2:
                if x != w - 1:
                    pole[y][w - x - 1][3] = col[d]
                    pole[y][w - x - 2][1] = col[d]
                    d += 1
                    if d == c:
                        d = 0
                    x += 1
        for i in range(h):
            for j in range(w):
                for k in range(4):
                    if pole[i][j][k] == 'n':
                        a = random.randint(0, c * 2 - 1)
                        if a != c * 2 - 1:
                            if k == 1:
                                pole[i][j][k] = col[(a // 2)]
                                pole[i][j + 1][3] = col[(a // 2)]
                            if k == 2:
                                pole[i][j][k] = col[(a // 2)]
                                pole[i + 1][j][0] = col[(a // 2)]
    if l == 2:
        b = random.randint(1, 2) # 1 - Вверх, 2 - Вправо
        if b == 1:
            e = random.randint(1, w - 2)
        if b == 2:
            e = random.randint(1, h - 2)
        while x != w - 1 or y != h - 1:
            if b == 0:
                a = random.randint(1, 2) # 1 - Вниз, 2 - Влево
                if a == 1:
                    if y != h - 1:
                        pole[y][w - x - 1][2] = col[d]
                        pole[y + 1][w - x - 1][0] = col[d]
                        d += 1
                        if d == c:
                            d = 0
                        y += 1
                if a == 2:
                    if x != w - 1:
                        pole[y][w - x - 1][3] = col[d]
                        pole[y][w - x - 2][1] = col[d]
                        d += 1
                        if d == c:
                            d = 0
                        x += 1
                    if x == e:
                        if y != 0:
                            y -= 1
                            pole[y][w - x - 1][2] = col[d]
                            pole[y + 1][w - x - 1][0] = col[d]
                            d += 1
                            if d == c:
                                d = 0
                            pole[y][w - x - 1][3] = col[d]
                            pole[y][w - x - 2][1] = col[d]
                            x += 1
                            d += 1
                            if d == c:
                                d = 0
            if b == 2 or b == 1:
                a = random.randint(1, 2) # 1 - Вниз, 2 - Влево
                if a == 1:
                    if y != h - 1:
                        pole[y][w - x - 1][2] = col[d]
                        pole[y + 1][w - x - 1][0] = col[d]
                        d += 1
                        if d == c:
                            d = 0
                        y += 1
                    if y == e:
                        if x != 0:
                            x -= 1
                            pole[y][w - x - 1][3] = col[d]
                            pole[y][w - x - 2][1] = col[d]
                            d += 1
                            if d == c:
                                d = 0
                            pole[y][w - x - 1][2] = col[d]
                            pole[y + 1][w - x - 1][0] = col[d]
                            y += 1
                            d += 1
                            if d == c:
                                d = 0
                if a == 2:
                    if x != w - 1:
                        pole[y][w - x - 1][3] = col[d]
                        pole[y][w - x - 2][1] = col[d]
                        d += 1
                        if d == c:
                            d = 0
                        x += 1
        for i in range(h):
            for j in range(w):
                for k in range(4):
                    if pole[i][j][k] == 'n':
                        a = random.randint(0, c * 2 - 1)
                        if a != c * 2 - 1:
                            if k == 1:
                                pole[i][j][k] = col[(a // 2)]
                                pole[i][j + 1][3] = col[(a // 2)]
                            if k == 2:
                                pole[i][j][k] = col[(a // 2)]
                                pole[i + 1][j][0] = col[(a // 2)]
    return pole

def generate_pole(size, colors):
    # Пока пусть возвращает это поле, потом добавим алгоритм
    colors = list(var.COLOR_VALUE.keys())[: colors]
    pole = read_pole(var.FILENAME[var.CHLVL], 0)
    return pole, colors
