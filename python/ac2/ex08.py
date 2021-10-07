from random import randint

# functions 

def title(msg):
    return '*' * 45 + '\n' + msg + '\n' + '*' * 45

def menu():
    str = '\n1. Adição\n' + '2. Subtração\n' + '3. Multiplicação\n' + '4. Divisão Inteira\n' + '5. Sair\n'
    return str

def question(type):
    a = randint(1, 10)
    b = randint(1, 10)

    if type == '1':
        print(a, ' + ', b, ' = ?')
        resp = float(input('resposta:'))
        if resp == a + b:
            return True
        else:
            return False
    if type == '2':
        print(a, ' - ', b, ' = ?')
        resp = float(input('resposta:'))
        if resp == a - b:
            return True
        else:
            return False
    if type == '3':
        print(a, ' * ', b, ' = ?')
        resp = float(input('resposta:'))
        if resp == a * b:
            return True
        else:
            return False
    if type == '4':
        print(a, ' // ', b, ' = ?')
        resp = float(input('resposta:'))
        if resp == a // b:
            return True
        else:
            return False

count = 0
tentativas = 0

# main flow
while True:
    print(title("Um questionátrio simples de matemática"))
    print(menu())
    answer = input('Digite sua escolha: ')

    if answer == '1':
        if question(answer):
            count += 1
            tentativas +=1
        else:
            tentativas +=1
            
    elif answer == '2':
        if question(answer):
            count += 1
            tentativas +=1
        else:
            tentativas +=1
    elif answer == '3':
        if question(answer):
            count += 1
            tentativas +=1
        else:
            tentativas +=1
    elif answer == '4':
        if question(answer):
            count += 1
            tentativas +=1
        else:
            tentativas +=1
    elif answer == '5':
        break
    else:
        print('-' * 50)
        print('\nOperação inválida, digite novamente!\n')
        print('-' * 50)

print('acertou: ', (count * 100) / tentativas, '%')
print('Bye!')
