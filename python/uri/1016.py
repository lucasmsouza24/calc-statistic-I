vm1 = 60
vm2 = 90 

vm3_km_h = abs(vm1 - vm2)
vm3_km_min = vm3_km_h / 60 

distance = int(input())
time_min = distance / vm3_km_min

print(f'{int(time_min)} minutos')