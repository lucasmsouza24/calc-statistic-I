# reading values
values = input()
A, B, C = values.split(' ')
A, B, C = float(A), float(B), float(C)

pi = 3.14159

# calc
a = (A * C) / 2             # área do triangulo retângulo
b = pi * C ** 2             # área do círculo
c = (1 / 2) * C * (A + B)   # área do trapézio 
d = B ** 2                  # área do quadrado
e = A * B                   # área do retangulo 

# display
print(f'TRIANGULO: {a:.3f}\nCIRCULO: {b:.3f}\nTRAPEZIO: {c:.3f}\nQUADRADO: {d:.3f}\nRETANGULO: {e:.3f}')