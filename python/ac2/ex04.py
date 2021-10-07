def soma_lista(lista):
    acumulador = 0
    for i in lista:
        acumulador += i
    return acumulador 

amostra = [100, 300, 300, 400, 0, 500]

print(soma_lista(amostra))