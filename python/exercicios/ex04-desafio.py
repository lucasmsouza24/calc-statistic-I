import psutil
import time  

# título
def title(title):
    print('=' * 15, f' {title} ', '=' * 15)

# capturando dados de cpu
def get_cpu():
    data = {"use": psutil.cpu_percent(), "freq": psutil.cpu_freq().current / 1000}
    return data

# main
i = 0
# while True:
while i <= 3:
    # armazenando dados
    cpu = get_cpu()
    
    # exibindo dados
    title('CPU')
    print('Uso da cpu: ', cpu["use"], '%')
    print('Frequencia: ', cpu['freq'], 'Ghz')

    # incremento temporario
    i += 1

    # zzzZZZ
    time.sleep(2)