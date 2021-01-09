import Variables as var
import random

def read_pole(filename, flag):
    f = open(filename, 'r')
    g = f.readlines()
    a = []
    width = 0
    height = 0
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
    else:
        return width, height

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
    pole = generate_random_pole(11, 7, 4, 2)
    #pole = read_pole(var.FILENAME, 0)
    #pole = [
        #[['s', 'b', 'n', 's'], ['s', 'b', 'n', 'b'], ['s', 'r', 'n', 'b'], ['s', 'b', 'g', 'r'], ['s', 'r', 'n', 'b'],
         #['s', 's', 'r', 'r']],
        #[['n', 'r', 'b', 's'], ['n', 'r', 'n', 'r'], ['n', 'g', 'b', 'r'], ['g', 'b', 'r', 'g'], ['n', 'g', 'n', 'b'],
         #['r', 's', 'b', 'g']],
        #[['b', 'g', 'n', 's'], ['n', 'b', 'n', 'g'], ['b', 'b', 'g', 'b'], ['r', 'g', 'r', 'b'], ['n', 'r', 'n', 'g'],
         #['b', 's', 'n', 'r']],
        #[['n', 'r', 'b', 's'], ['n', 'b', 'g', 'r'], ['g', 'n', 'r', 'b'], ['r', 'b', 'n', 'n'], ['n', 'n', 'g', 'b'],
         #['n', 's', 'g', 'n']],
        #[['b', 'r', 's', 's'], ['g', 'b', 's', 'r'], ['r', 'b', 's', 'b'], ['n', 'g', 's', 'b'], ['g', 'r', 's', 'g'],
         #['g', 's', 's', 'r']]]
    return pole, colors

