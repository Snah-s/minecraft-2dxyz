from colorama import Back, Style, Fore, init

init(autoreset=True)

va = Back.WHITE + "    " + Style.RESET_ALL
wh = Back.WHITE + "    " + Style.RESET_ALL
bl = Back.BLACK + "    " + Style.RESET_ALL
gr = Back.GREEN + "    " + Style.RESET_ALL
ye = Back.YELLOW + "    " + Style.RESET_ALL
re = Back.RED + "    " + Style.RESET_ALL
bu = Back.BLUE + "    " + Style.RESET_ALL
lb = Back.LIGHTBLACK_EX + "    " + Style.RESET_ALL
cy = Back.CYAN + "    " + Style.RESET_ALL
ma = Back.MAGENTA + "    " + Style.RESET_ALL


def create_empty_world():
    mapa = [[va for j in range(42)] for i in range(21)]
    for i in range(len(mapa)):
        if i == 0:
            for j in range(len(mapa[i])):
                mapa[i][j] = str(j)
    for j in range(42):
        if j == 0:
            for i in range(len(mapa)):
                mapa[i][j] = str(i)
    mapa[0][0] = '    '
    return mapa


def draw_empty_world():
    mapa = create_empty_world()
    for r in range(len(mapa)):
        for c in range(len(mapa[r])):
            if c < 31:
                print(mapa[r][c].center(4), end='')
            elif c == 31:
                print()


def create_full_world():
    mapa = create_empty_world()
    for i in range(len(mapa)):
        if i == 1 or i == 3:
            for j in range(len(mapa[i])):
                if 27 < j < 31:
                    mapa[i][j] = ye
        elif i == 2:
            for j in range(len(mapa[i])):
                if 26 < j < 32:
                    mapa[i][j] = ye
        elif i == 4:
            for j in range(len(mapa[i])):
                if 20 < j < 24 or 35 < j < 39:
                    mapa[i][j] = gr
                elif 27 == j or 29 == j or 31 == j:
                    mapa[i][j] = ye
        elif i == 13:
            for j in range(len(mapa[i])):
                if 0 < j < 26 or 28 < j < 41:
                    mapa[i][j] = gr
        elif 13 < i < 21:
            for j in range(len(mapa[i])):
                if 0 < j:
                    mapa[i][j] = bl
        elif i == 6:
            for j in range(len(mapa[i])):
                if 18 < j < 26 or 33 < j < 41:
                    mapa[i][j] = gr
        elif i == 5:
            for j in range(len(mapa[i])):
                if 19 < j < 25 or 34 < j < 40:
                    mapa[i][j] = gr
        elif i == 7:
            for j in range(len(mapa[i])):
                if 3 < j < 7 or 9 < j < 13 or 15 < j < 19:
                    mapa[i][j] = gr
        elif i == 8:
            for j in range(len(mapa[i])):
                if 2 < j < 8 or 8 < j < 14 or 14 < j < 20 or j == 25 or j == 29 or j == 39:
                    mapa[i][j] = gr
        elif i == 9:
            for j in range(len(mapa[i])):
                if 23 < j < 27 or 27 < j < 31 or 37 < j < 41:
                    mapa[i][j] = gr
        elif i == 12:
            for j in range(len(mapa[i])):
                if 12 == j or 15 == j or 20 == j or 30 == j or 35 == j:
                    mapa[i][j] = lb
    mapa[3][22] = gr
    mapa[3][37] = gr
    mapa[17][2] = lb
    mapa[14][5] = lb
    mapa[18][5] = lb
    mapa[16][7] = lb
    mapa[19][7] = lb
    mapa[16][10] = lb
    mapa[19][29] = lb
    mapa[15][25] = lb
    mapa[19][15] = lb
    mapa[16][34] = lb
    mapa[16][37] = lb
    mapa[18][37] = lb
    mapa[18][40] = lb
    for j in range(41):
        if j == 22 or j == 37:
            for i in range(len(mapa)):
                if 6 < i < 13:
                    mapa[i][j] = re
        elif 25 < j < 29:
            for i in range(len(mapa)):
                if 12 < i < 18:
                    mapa[i][j] = bu
        elif 5 == j or 11 == j or 17 == j:
            for i in range(len(mapa)):
                if 8 < i < 13:
                    mapa[i][j] = re
                elif i == 6:
                    mapa[i][j] = gr
        elif 25 == j or 29 == j or 39 == j:
            for i in range(len(mapa)):
                if 9 < i < 13:
                    mapa[i][j] = re
        elif 23 == j:
            for i in range(len(mapa)):
                if 14 < i < 19:
                    mapa[i][j] = lb
        elif 9 == j or 7 == j:
            for i in range(len(mapa)):
                if 10 < i < 13:
                    mapa[i][j] = lb
        elif 8 == j:
            for i in range(len(mapa)):
                if 9 < i < 13:
                    mapa[i][j] = lb
        elif 16 == j:
            for i in range(len(mapa)):
                if 10 < i < 13:
                    mapa[i][j] = lb
    return mapa


def draw_world():
    mapa = create_full_world()
    for r in range(len(mapa)):
        for c in range(len(mapa[r])):
            if c < 31:
                print(mapa[r][c].center(4), end='')
            elif c == 31:
                print()


def create_player():
    mapa = create_full_world()
    mapa[10][2] = cy
    mapa[11][2] = cy
    mapa[12][2] = cy
    mapa[11][3] = ma
    return mapa


def draw_player():
    mapa = create_player()
    for r in range(len(mapa)):
        for c in range(len(mapa[r])):
            if c < 31:
                print(mapa[r][c].center(4), end='')
            elif c == 31:
                print()


def move_player(option):
    mapa = create_player()
    x = 0
    y = 0
    mv = 0
    for i in option:
        if str(i).lower() == 'left':
            x = x - 1
        elif str(i).lower() == 'right':
            x = x + 1
        elif str(i).lower() == 'up':
            y = y - 1
        elif str(i).lower() == 'down':
            y = y + 1
    if (-2 < x < 38) and (-9 < y < 2):
        mapa[11][2] = va
        mapa[10][2] = va
        mapa[12][2] = va
        mapa[11][3] = va
        mapa[11 + y][2 + x] = cy
        mapa[10 + y][2 + x] = cy
        mapa[12 + y][2 + x] = cy
        mapa[11 + y][3 + x] = ma
        for i in range(x): #x es lo que ingresamos por teclado ejm: x = 22
            if 19 < i < 30: # i va desde 0 hasta x-1, ejm: el maximo valor de i = 21
                mv = mv + 1 #mv en 20 se suma 1 y mv en 21 se suma 1 lo que hace que mv= 2
    return mapa, mv


def actions(option):
    mapa, mv = move_player(option)
    x = 0
    y = 0
    wood = 0
    stone = 0
    for i in option:
        if str(i).lower() == 'left':
            x = x - 1
        elif str(i).lower() == 'right':
            x = x + 1
        elif str(i).lower() == 'up':
            y = y - 1
        elif str(i).lower() == 'down':
            y = y + 1
        elif str(i).lower() == "destroy":
            if (-2 < x < 38) and (-9 < y < 2):
                if mapa[11 + y][3 + x] == ye:
                    mapa[11 + y][3 + x] = va
                elif mapa[11 + y][3 + x] == bu:
                    mapa[11 + y][3 + x] = va
                elif mapa[11 + y][3 + x] == bl:
                    mapa[11 + y][3 + x] = va
                elif mapa[11 + y][3 + x] == gr:
                    mapa[11 + y][3 + x] = va
                elif mapa[11 + y][3 + x] == re:
                    mapa[11 + y][3 + x] = va
                elif mapa[11 + y][3 + x] == lb:
                    mapa[11 + y][3 + x] = va
        elif str(i).lower() == 'extract':
            if (-2 < x < 38) and (-9 < y < 2):
                if mapa[11 + y][3 + x] == re:
                    wood += 1
                    mapa[11 + y][3 + x] = va
                elif mapa[11 + y][3 + x] == lb:
                    stone += 1
                    mapa[11 + y][3 + x] = va
        elif str(i).lower() == 'build wood':
            if (-2 < x < 38) and (-9 < y < 2) and (0 < wood):
                if mapa[11 + y][3 + x] == va:
                    mapa[11 + y][3 + x] = re
                    wood -= 1
        elif str(i).lower() == 'build stone':
            if (-2 < x < 38) and (-9 < y < 2) and (0 < stone):
                if mapa[11 + y][3 + x] == va:
                    mapa[11 + y][3 + x] = lb
                    stone -= 1
    return mapa, wood, stone, mv


def draw_actions(option):
    l = [] #lo que sale al final: ["right", "right", "extract", "up", "extract"] asÃ­
    n = option.split(',')
    g = [] # lo previo: [['19', 'right'], 'extract', ['1', 'up'], 'extract', ['1', 'up']]
    for i in range(len(n)):
        if n[i].strip()[0].isdigit(): #strip le quita los espacios #is digit retorna true si hay un numero
            g.append(n[i].split())
        else:
            g.append(n[i].strip())
    for i in g:
        if i[0].isdigit() and 1 < len(i):
            for j in range(int(i[0])):
                l.append(i[1])
        else:
            l.append(i)
    mapa, wood, stone, mv = actions(l)
    print()
    for r in range(len(mapa)):
        for c in range(len(mapa[r])):
            if c == 0:
                print(mapa[r][c].center(4), end='')
            if mv < c < 31 + mv: #del ejemplo anterior, mv = 2 "c es la columna" y se imprime desde la columna 3
                print(mapa[r][c].center(4), end='') # hasta la columna 30 + mv = 32
            elif c == 31 + mv: # c == en la fila 31 + 2 = )33( se hace el salto de linea
                print()
    print('Wood: \t', wood)
    print('Stone: \t', stone)


primer_comando = input("$ ")
while primer_comando.strip() != "init":
    primer_comando = input("$ ")
if primer_comando.strip() == "init":
    print("$ Welcome to the minecraft 2d xyz world".center(120))
    print()
    draw_player()

c = input("$ ")
j = ""
while j != "end":
    j = input("$ ")
    c += "," + j

draw_actions(c)
"""
19 right, extract, 1 up, extract, 1 up, extract, 1 up, extract, 1 up, extract, 5 down, extract
4 right, build wood, 1 right, build wood, 1 right, build wood, 5 up
"""
