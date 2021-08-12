import psutil as ps

# cpu_times
print('=' * 50)
print("cpu_times: ", ps.cpu_times(percpu=False))
print("user: ", ps.cpu_times(percpu=False).user)
print("system: ", ps.cpu_times(percpu=False).system)
print("idle: ", ps.cpu_times(percpu=False).idle)
print("interrupt: ", ps.cpu_times(percpu=False).interrupt)
print("dpc: ", ps.cpu_times(percpu=False).dpc)

# cpu_percent
print('=' * 50)
print("cpu_percent:", ps.cpu_percent(interval=1))

# cpu_count()
print('=' * 50)
print("cpu_count: ", ps.cpu_count())
print("cpu_count(logical=True): ", ps.cpu_count(logical=True))
print("cpu_count(logical=False): ", ps.cpu_count(logical=False))

# freq
print('=' * 40)
print("cpu_freq: ", ps.cpu_freq())
print("current: ", ps.cpu_freq().current)
print("min: ", ps.cpu_freq().min)
print("max: ", ps.cpu_freq().max)

# disk_usage
print('=' * 40)
print("disk_usage: ", ps.disk_usage('/'))
print("total: ", ps.disk_usage('/').total)
print("used: ", ps.disk_usage('/').used)
print("free: ", ps.disk_usage('/').free)
print("percent: ", ps.disk_usage('/').percent)