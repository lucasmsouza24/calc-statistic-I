# datasets
user_thor = ['mysql', 'CPU', 'RAM', 'SSD1', 'Google']
user_thanos = ['LoL', 'RAM', 'CPU', 'HD', 'Google']
user_cap = ['mysql', 'LoL', 'RAM', 'CPU', 'Firefox']
user_tony = ['mysql', 'CPU', 'RAM', 'SSD1', 'Google']

user_thor = set(user_thor)
user_thanos = set(user_thanos)
user_cap = set(user_cap)
user_tony = set(user_tony)

# pertinencia
print('CPU' in user_tony)
print('Firefox' in user_thanos)
print('LoL' not in user_thor)
print('LoL' not in user_thanos)
print(user_thor.issubset(user_thanos))
print(user_thor.issubset(user_tony))
print(user_thor <= user_tony)
print(user_thor <= user_thanos)
print(user_tony.issuperset(user_thor))
print(user_tony >= user_thor)

# igualdade / comparação
print(user_tony ==(user_thor))
print(user_tony !=(user_thor))
print(user_tony ==(user_cap))
print(user_tony !=(user_cap))

# diferença simétrica
# Um novo conjunto surge, contendo todos os elementos
# que não são comuns aos dois conjuntos. 
print(user_tony ^ user_cap)
