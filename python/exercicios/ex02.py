import random
import matplotlib.pyplot as plt

def imc(peso, altura):
    return peso / pow(altura, 2)

def diagnostico(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif 18.5 <= imc <25:
        return 'Peso normal'
    elif 25 <= imc <30:
        return 'Sobrepeso'
    elif 30 <= imc <40:
        return 'Obesidade'
    elif imc >=40:
        return 'Obesidade mórbida'

pessoas = int(input('Simular IMC de quantas pessoas? '))

pesos = []
alturas = []
imcs = []
diagnosticos = []

for i in range(0, pessoas):

    altura = random.uniform(1.53, 1.95)
    peso = random.uniform(48, 100)

    alturas.append(altura)
    pesos.append(peso)
    imcs.append(imc(peso, altura))
    diagnosticos.append(diagnostico(imc(peso, altura)))

for i in range(0, len(imcs)):
    print('Pessoa {}\n'.format(i + 1))
    print('altura: {:.2f}'.format(alturas[i]))
    print('peso: {:.2f}'.format(pesos[i]))
    print('IMC: {:.2f}'.format(imcs[i]))
    print('Diagnóstico: {}'.format(diagnosticos[i]))
    print('=' * 70)

print('Pessoas consultadas: {}'.format(len(imcs)))
print('IMC médio: {:.2f}'.format(sum(imcs) / len(imcs)))

# brunao que fez
plt.hist(imcs)
plt.show()