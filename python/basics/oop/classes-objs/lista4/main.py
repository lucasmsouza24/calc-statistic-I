from bolo import Bolo 

b1 = Bolo('abacaxi', 14)
b2 = Bolo('chocolate', 20)
b3 = Bolo('morango', 16)

bolos = [b1, b2, b3]

def exibeMenu():
    for i in range(0, len(bolos) + 1):
        if i < len(bolos):
            print(f'[{i + 1}] {bolos[i].sabor}')
        else:
            print(f'[{i + 1}] sair')

while True:
    print('=' * 20)
    exibeMenu()
    opcao_escolhida = int(input('\nescolha uma opção: '))

    if opcao_escolhida <= len(bolos):
        qtd = int(input('escolha a quantidade: '))
        bolos[opcao_escolhida - 1].comprar_bolo(qtd)
        continue
    else:
        break

# exibindo relatório de todos os bolos
total = 0
for bolo in bolos:
    bolo.exibir_relatorio()
    total += bolo.total_faturado()

print(f'\ntotal faturado: R$ {total:.2f}')