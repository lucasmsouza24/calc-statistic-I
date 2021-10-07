from math import floor

segunda_a_quarta = 8.5 # horas
quinta_a_sexta = 9 # horas
semanas_trabalhadas = 4
remuneracao = 5468 # R$
remuneracao_semanal = remuneracao / 4
horas_semanais = (segunda_a_quarta * 3) + (quinta_a_sexta * 2)
remuneracao_por_hora = remuneracao_semanal / horas_semanais
piso_salarial = floor(remuneracao_por_hora)

print(piso_salarial)