import psutil

cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage} %")

memory = psutil.virtual_memory()
print(f"Memory Usage: {memory.percent} %")

disk_c = psutil.disk_usage("C:\\")
disk_d = psutil.disk_usage("D:\\")

print(f"Disk Usage (C:): {disk_c.percent} %")
print(f"Disk Usage (D:): {disk_d.percent} %")
