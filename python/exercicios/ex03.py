import matplotlib.pyplot as plt
import psutil as psu

# definindo hardware que será monitorado
def menu():
    print('=' * 40)
    print('Selecione o dispositivo a ser monitorado:')
    print('[1] Tempo de CPU')
    print('[2] Frequência de CPU')
    print('[3] Disco')
    print('[4] Sair')
    answer = int(input())
    return answer

# Exibe informações sobre o tempo da cpu
def cpu_time():
    # capturando dados dos componentes (minutos)
    data = psu.cpu_times(percpu=False)
    user = round((data.user / 60), 1)
    system = round((data.system / 60), 1)
    idle = round((data.idle / 60), 1)
    interrupt = round((data.interrupt / 60), 1)
    dpc = round((data.dpc / 60), 1)

    # exibindo dados no terminal
    print('=' * 40)
    print(f'user: {hour_formater(user)}')
    print(f'system: {hour_formater(system)}')
    print(f'idle: {hour_formater(idle)}')
    print(f'interrupt: {hour_formater(interrupt)}')
    print(f'dpc: {hour_formater(dpc)}')

    # exibindo dados através de um gráfico
    labels = ['User', 'System', 'Idle', 'Interrupt', 'dpc']
    bars = [user, system, idle, interrupt, dpc]
    plt.bar(labels, bars)
    plt.show()

# Exibe informações sobre frequência da cpu
def cpu_freq(clock):
    data = psu.cpu_freq()
    pct = psu.cpu_percent(interval=0.8) # uso da cpu em %

    # convertendo dados de Bytes para GB
    current = round(data.current / 1000, 1)
    min = round(data.min / 1000, 1)
    max = round(data.max / 1000, 1)

    # Exibindo dados no terminal
    print('=' * 40)
    print(f'Aguarde {10 - clock} segundos...')
    print(f'current: {current} GHz')
    print(f'cpu percent: {pct} %')
    print(f'min: {min} GHz')
    print(f'max: {max} GHz')
    return pct

# Exibe informações sobre o estado atual da cpu
def cpu_state():
    percent = []
    print('=' * 40)
    print('Analisando Frequencia da CPU')

    # captura do uso da CPU em %
    for i in range(0, 10):
        percent.append(cpu_freq(i + 1))
    
    # Exibição dos dados em gráfico
    plt.plot(percent, 'go-', label='coe')
    plt.show()
    
# captura de dados de disco
def disk():
    data = psu.disk_usage('/')
    total = round(data.total / 1e+9, 1)
    used = round(data.used / 1e+9, 1)
    free = round(data.free / 1e+9, 1)

    # Exibição de dados no terminal
    print('=' * 40)
    print('Disco')
    print(f'Total: {total} GB')
    print(f'Em uso: {used} GB ({data.percent} %)')
    print(f'Espaço livre: {free} GB')

    # Exibição de dados em gráfico
    labels = ['Total', 'Em uso', 'Espaço livre']
    bars = [total, used, free]
    plt.bar(labels, bars)
    plt.show()

# formatador de minutos para horas+min
def hour_formater(min):
    hours = min // 60
    mins = min % 60
    return f'{hours:.0f}h{mins:.0f}min'

# definição do fluxo do programa
while True:
    answer = menu()
    if answer == 4:
        print('=' * 40)
        print('Bye!')
        print('=' * 40)
        break;
    elif answer == 1:
        cpu_time()
    elif answer == 2:
        cpu_state()
    elif answer == 3:
        disk()
    else:
        print('=' * 40)
        print('Escolha inválida')
