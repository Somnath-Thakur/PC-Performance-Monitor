import psutil
import time

cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage} %")

memory = psutil.virtual_memory()
print(f"Memory Usage: {memory.percent} %")

disk_c = psutil.disk_usage("C:\\")
disk_d = psutil.disk_usage("D:\\")

print(f"Disk Usage (C:): {disk_c.percent} %")
print(f"Disk Usage (D:): {disk_d.percent} %")


network1 = psutil.net_io_counters()

time.sleep(1)

network2 = psutil.net_io_counters()

download_speed = (network2.bytes_recv - network1.bytes_recv) / (1024)**2
upload_speed = (network2.bytes_sent - network1.bytes_sent) / (1024)**2

print(f"Download Speed: {download_speed:.2f} MB/s")
print(f"Upload Speed: {upload_speed:.2f} MB/s")