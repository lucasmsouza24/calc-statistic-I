def read_point():
    x, y = input().split(' ')
    return [float(x), float(y)]

x1, y1 = read_point()
x2, y2 = read_point()

distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1 / 2)

print(f'{distance:.4f}')