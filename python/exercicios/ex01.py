# 1) Exercício 1
print('\n','='*90, '\n')
print('1) para a = 2, atribua as potencias de 2, 3, 4 e imprima seus valores.\n')

a = 2
potencia_ao_quadrado = a ** 2
potencia_ao_cubo = a ** 3
potencia_a_quarta = a ** 4

print('a ** 2 = ', potencia_ao_quadrado)
print('a ** 3 = ', potencia_ao_cubo)
print('a ** 4 = ', potencia_a_quarta)
print('\n','='*90, '\n')

# Exercício 2
print('2) para x = 512, atribua e exiba as raizes: quadrada, cubica e quarta de x.\n')

x = 512
raiz_quadrada_de_x = pow(x, 1/2)
raiz_cubica_de_x = pow(x, 1/3)
raiz_quarta_de_x = pow(x, 1/4)

print('Raiz quadrada de x = ', raiz_quadrada_de_x)
print('Raiz cubica de x = ', raiz_cubica_de_x)
print('Raiz quarta de x = ', raiz_quarta_de_x)
print('\n','='*90, '\n')

# Exercício 3
print('3) para w = 3345.61. importe as funções floor e ceil da biblioteca math e determine o piso, o teto e o arredondamento de w.\n')

w = 3345.61
from math import floor, ceil
piso = floor(w)
teto = ceil(w)
arredondamento = round(w)

print('piso = ', piso)
print('teto = ', teto)
print('arredondamento = ', arredondamento)
print('\n','='*90, '\n')

# Exercício 4
print('4.1) Por que não importamos o round?\n')
print('Resposta: Além do round não fazer parte da biblioteca Math, ele é um método padrão do python, por isso não precisa ser importado.\n')

print('4.2) Explique a saída do seguinte comando.\n')
print('>>> round(w, 1)')
print(round(w, 1), '\n')
print('Resposta: O método round() arredondou w para cima, pois sua primeira casa decimal é maior que 5')
print('\n','='*90, '\n')

# Exercício 5
print('5) Arredonde os números a seguir, deixando ndigits = none')
print('x1 = 1.456  ', '  x2 = 3.678  ', '  x3 = 7.5\n')

x1 = 1.456
x2 = 3.678
x3 = 7.5

print('x1 = ', round(x1))
print('x2 = ', round(x2))
print('x3 = ', round(x3))
print('\n','='*90, '\n')

# Exercício 6
print('6) Voltando ao caso do floor e ceil, por padrão estas funções retornam valores decimais, ou seja, com ponto flutuante.\n Podemos determinar que ambas funções resultem em uma saída com inteiro mantendo a mesma característica de piso e teto.\n Faça o teste com o comando a seguir:\n')

print('>>> int(floor(1.456))')
print(int(floor(1.456)))
print('\n','='*90, '\n')

# Exercício 7
print('7) Resolva as expressões a seguir:\n')
print('a) pow(2, 3) = ', pow(2, 3))
print('b) pow(-2, 3) = ', pow(-2, 3))
print('c) pow(1, 0) = ', pow(1, 0))
print('d) pow(-1, 0) = ', pow(-1, 0))
print('e) pow(2, 0) = ', pow(2, 0))
print('f) pow(2/5, 3) = ', pow(2/5, 3))
print('g) pow(3, -2) = ', pow(3, -2))
print('h) pow(1/2, -3) = ', pow(1/2, -3))
print('i) pow(pow(-1, 3), 4) = ', pow(pow(-1, 3), 4))
print('j) pow(0.5, 3) = ', pow(0.5, 3))
print('k) pow(0.25, 4) = ', pow(0.25, 4))
print('l) pow(0, 4) = ', pow(0, 4))
print('m) 1 + pow(0.41, 2) = ', 1 + pow(0.41, 2))
print('n) (1/4) + pow(5, 2) - pow(2, -4) = ', 1/4 + pow(5, 2) - pow(2, -4))
print('o) pow((4/5) - (1/2) + 1, -2) + (1 / (1 + pow(3, 2) - pow(4 - 5, -2)))', pow((4/5) - (1/2) + 1, -2) + (1 / (1 + pow(3, 2) - pow(4 - 5, -2))))