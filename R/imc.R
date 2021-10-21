nome <- readline(prompt = "Digite seu nome: ")

peso <- readline(prompt="informe seu peso: ")
peso <- as.double(peso)

altura <- readline(prompt="Informe sua altura: ")
altura <- as.double(altura)

imc <- peso / (altura * altura)
imc2 <- round(imc, 1)
print(imc2)

print(typeof(nome))
print(typeof(peso))