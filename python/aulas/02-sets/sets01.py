# conjunto_processador = {'CPU', 'Registrador', 'Core'}
# print(conjunto_processador)

# conjunto_processador = set(['CPU', 'Registrador', 'Core'])
# print(conjunto_processador)

# metricas_tunnel = {'CPU', 'RAM', 'Disco'}
# print(metricas_tunnel)

# cores = ['red', 'red', 'blue', 'green', 'yellow', 'orange', 'white']
# cores = set(cores)
# print(cores)
def show(txt, setx):
    print(f'\n{txt}: \n', setx)


user_thor = ['mysql', 'CPU', 'RAM', 'SSD1', 'Google']
user_thanos = ['LoL', 'RAM', 'CPU', 'HD', 'Google']
user_cap = ['mysql', 'LoL', 'RAM', 'CPU', 'Firefox']
user_tony = ['mysql', 'CPU', 'RAM', 'SSD1', 'Google']

user_thor = set(user_thor)
user_thanos = set(user_thanos)
user_cap = set(user_cap)
user_tony = set(user_tony)

print('thor: ', user_thor)
print('thanos: ', user_thanos)
print('cap: ', user_cap)
print('tony: ', user_tony)

print()

# união |
inventario1 = user_thor | user_cap
print('\nthor U cap: ', inventario1)

inventario2 = user_thor | user_cap | user_thanos | user_tony
print('\nthor U cap U tony U thanos:\n', inventario2)

inventario3 = user_thor.union(user_cap)
print('\nthor U cap: \n', inventario3)

# ex 01
result = user_thor.union(user_cap.union(user_thanos.union(user_tony)))
print("\nresult1:\n", result)

result2 = user_thor.union(user_cap, user_thanos, user_tony)
print('\nresult2: \n', result2)

result3 = user_tony | user_cap | user_thanos | user_thor
print('\nresult3: \n', result3)

result4 = user_thor.union(user_cap | user_thanos.union(user_tony))
print('\nresult4: \n', result4)

# intersecção
print('intersecçãon\n', '=' * 30)

result1 = user_thor & user_cap
print('\nresult1: \n', result1)

result2 = user_thor.intersection(user_cap)
print('\nresult2: \n', result2)

# ex02
print('ex02\n', '=' * 30)

result1 = user_thor.intersection(user_cap, user_thanos, user_tony)
print('\nresult1:\n', result1)

result2 = user_thanos & user_cap & user_thor & user_tony
show('result2', result2)

# diferença
diff1 = user_thor - user_thanos
show('diff1', diff1)

# ex03
diff = user_thor - user_thanos - user_cap - user_tony
show('diff', diff)

# pertinencia
print('\ncpu in tony:')
print('CPU' in user_tony)

print('\nfirefox in thanos:')
print('Firefox' in user_thanos)

print('\nlol in thanos:')
print('LoL' not in user_thanos)

print('\nSSD1 not in thor:')
print('SSD1' not in user_thor)

print('\nDISCO in thor:')
print('DISCO' in user_thanos)

print(user_thor)

