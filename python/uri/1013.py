def max(array):
    for i in range(0, len(array)):
        if i == 0:
            maior = array[i]
        elif array[i] > maior:
            maior = array[i]
    return maior 

# read inputs
a, b, c = input().split(' ')
a, b, c = int(a), int(b), int(c)

# calc
maior = max([a, b, c])

# display
print(f'{maior} eh o maior')