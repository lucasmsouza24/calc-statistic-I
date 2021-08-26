# metricas
import psutil

print(psutil.cpu_times(), '\n\n') # segundos
print(psutil.cpu_times(True), '\n\n')

print('\nuso de cada nucleo: ', psutil.cpu_percent(interval=0.5, percpu=True)) # percentual
print('\nnucleos fisicos: ', psutil.cpu_count(logical=False))
print('\nnucleos logicos: ', psutil.cpu_count(logical=True))

print('\nfreq:', psutil.cpu_freq().current) # Mhz

print('\nvirt mem: ', psutil.virtual_memory())

print('\nswap mem: ', psutil.swap_memory())

print('\n')