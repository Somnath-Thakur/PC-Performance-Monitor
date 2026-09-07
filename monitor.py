import psutil
import time
import os


while True:
    os.system("cls")
    print("\n==== PC Performance Monitor ====\n")
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


    processes = []

    for process in psutil.process_iter(["name", "memory_info"]):
        try:
            process_name = process.info["name"]
            memory_usage = process.info["memory_info"].rss / (1024 ** 2)  # Convert bytes to MB
            processes.append((process_name, memory_usage))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    processes.sort(key=lambda x: x[1], reverse=True)

    print("\nTop 5 Processes by Memory Usage:")

    for process_name, memory_usage in processes[:5]:
        print(f"Process: {process_name}, Memory Usage: {memory_usage:.2f} MB")

    time.sleep(1)

