def draw_carpet(w, h):

    for i in range(h):
        if i == 0 or i == h-1:
            for j in range(w):
                if j == 0 or j == w-1:
                    print('▓', end='')
                else:
                    print('░', end='')
        else:
            for z in range(w):
                if z == 0 or z == w-1:
                    print('▓', end='')
                elif z >= 2 and z <= w-3:
                    print('▒', end='')
                else:
                    print('░', end='')
        print()


draw_carpet(3, 3)
