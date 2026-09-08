import psutil
import time

print("--- PC Performance Monitor ---\n")

# Print the initial values
cpu_usage = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()

disk_c = psutil.disk_usage("C:\\")
disk_d = psutil.disk_usage("D:\\")

network1 = psutil.net_io_counters()
time.sleep(1)
network2 = psutil.net_io_counters()

download_speed = (network2.bytes_recv - network1.bytes_recv) / (1024)
upload_speed = (network2.bytes_sent - network1.bytes_sent) / (1024)

print(f"CPU Usage: {cpu_usage:.1f} %")
print(f"Memory Usage: {memory.percent:.1f} %")
print(f"Disk Usage (C:): {disk_c.percent:.1f} %")
print(f"Disk Usage (D:): {disk_d.percent:.1f} %")
print(f"Download Speed: {download_speed:.2f} KB/s")
print(f"Upload Speed: {upload_speed:.2f} KB/s")

# Get initial processes
processes = []

for process in psutil.process_iter(["name", "memory_info"]):
    try:
        process_name = process.info["name"]
        memory_usage = process.info["memory_info"].rss / (1024 ** 2)
        processes.append((process_name, memory_usage))
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        continue

processes.sort(key=lambda x: x[1], reverse=True)

for process_name, memory_usage in processes[:5]:
    print(f"Process: {process_name}, Memory Usage: {memory_usage:.2f} MB")


while True:

    # Get new values
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()

    disk_c = psutil.disk_usage("C:\\")
    disk_d = psutil.disk_usage("D:\\")

    network1 = psutil.net_io_counters()
    time.sleep(1)
    network2 = psutil.net_io_counters()

    download_speed = (network2.bytes_recv - network1.bytes_recv) / (1024)
    upload_speed = (network2.bytes_sent - network1.bytes_sent) / (1024)

    # Get processes
    processes = []

    for process in psutil.process_iter(["name", "memory_info"]):
        try:
            process_name = process.info["name"]
            memory_usage = process.info["memory_info"].rss / (1024 ** 2)
            processes.append((process_name, memory_usage))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    processes.sort(key=lambda x: x[1], reverse=True)

    # Move cursor back 11 lines
    print("\033[11A", end="")

    # Update CPU
    print("\033[2K", end="")
    print(f"CPU Usage: {cpu_usage:.1f} %")

    # Update RAM
    print("\033[2K", end="")
    print(f"Memory Usage: {memory.percent:.1f} %")

    # Update Disk C
    print("\033[2K", end="")
    print(f"Disk Usage (C:): {disk_c.percent:.1f} %")

    # Update Disk D
    print("\033[2K", end="")
    print(f"Disk Usage (D:): {disk_d.percent:.1f} %")

    # Update Download
    print("\033[2K", end="")
    print(f"Download Speed: {download_speed:.2f} KB/s")

    # Update Upload
    print("\033[2K", end="")
    print(f"Upload Speed: {upload_speed:.2f} KB/s")

    # Update top 5 processes
    for process_name, memory_usage in processes[:5]:
        print("\033[2K", end="")
        print(f"Process: {process_name}, Memory Usage: {memory_usage:.2f} MB")