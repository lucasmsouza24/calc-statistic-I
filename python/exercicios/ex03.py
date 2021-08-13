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
    return [answer]

# Exibe informações sobre o tempo da cpu
def cpu_time():
    data = psu.cpu_times(percpu=False)
    print('=' * 40)
    print("user: ", round((data.user / 60) / 60, 1), 'h')
    print("system: ", round((data.system / 60) / 60, 1), 'h')
    print("idle: ", round((data.idle / 60) / 60, 1), 'h')
    print("interrupt: ", round((data.interrupt / 60) / 60, 1), 'h')
    print("dpc: ", round((data.dpc / 60) / 60, 1), 'h')

# Exibe informações sobre frequência da cpu
def cpu_freq():
    data = psu.cpu_freq()
    print('=' * 40)
    print('Frequencia da CPU')
    print('current: ', round(data.current / 1000, 1), 'GHz')
    print('min: ', round(data.min / 1000, 1), 'GHz')
    print('max: ', round(data.max / 1000, 1), 'GHz')

def disk():
    data = psu.disk_usage('/')
    print('=' * 40)
    print('Disco')
    print('total: ', round(data.total / 1e+9, 1), 'GB')
    print('used: ', round(data.used / 1e+9, 1), 'GB')
    print('free: ', round(data.free / 1e+9, 1), 'GB')
    print('percent: ', data.percent, '%')

# main
while True:
    answer = menu()
    if answer[0] == 4:
        print('Bye!')
        break;
    elif answer[0] == 1:
        cpu_time()
    elif answer[0] == 2:
        cpu_freq()
    elif answer[0] == 3:
        disk()
