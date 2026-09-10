import time
import tkinter as tk
import psutil


window = tk.Tk()

window.title("PC Performance Monitor")
window.geometry("1920x1080")


title = tk.Label(
    window,
    text="PC Performance Monitor",
    font=("Arial", 20)
)

title.pack(pady=20)

def feature_label(text):
    label = tk.Label(
        window,
        text=text,
        font=("Arial", 12)
    )
    label.pack(pady=10)
    return label
        


def update_feature(get_data, label,feature_name):
    new_data = get_data()
    label.config(
        text=f"{feature_name}: {new_data:.1f}%"
    )

    window.after(1000, update_feature, get_data, label, feature_name)

cpu_label = feature_label("CPU Usage: 0%")
update_feature(lambda: psutil.cpu_percent(interval=None), cpu_label, "CPU Usage")


ram_label = feature_label("RAM Usage: 0%")
update_feature(lambda: psutil.virtual_memory().percent, ram_label, "RAM Usage")

disk_c_label = feature_label("Disk Usage (C:): 0%")
update_feature(lambda: psutil.disk_usage("C:\\").percent, disk_c_label, "Disk Usage (C:)")  

disk_d_label = feature_label("Disk Usage (D:): 0%")
update_feature(lambda: psutil.disk_usage("D:\\").percent, disk_d_label, "Disk Usage (D:)")

network_label = feature_label("Download Speed: 0 KB/s, Upload Speed: 0 KB/s")

process_label = []

for i in range(0,5):
    process_label.append(feature_label("Process: , Memory: "))



def update_network_speed():
    network1 = psutil.net_io_counters()
    time.sleep(1)       
    network2 = psutil.net_io_counters()
    download_speed = (network2.bytes_recv - network1.bytes_recv) / (1024)
    upload_speed = (network2.bytes_sent - network1.bytes_sent) / (1024)
    network_label.config(
        text=f"Download Speed: {download_speed:.2f} KB/s, Upload Speed: {upload_speed:.2f} KB/s"
    )
    network1 = network2
    window.after(1000, update_network_speed)


def update_process():
    processes = []
    for process in psutil.process_iter(["name", "memory_info"]):
        try:
            process_name = process.info["name"]
            memory_usage = process.info["memory_info"].rss / (1024 ** 2)
            processes.append((process_name, memory_usage))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    processes.sort(key=lambda x: x[1], reverse=True)

    for i, (process_name, memory_usage) in enumerate(processes[:5]):
        process_label[i].config(
            text = f"Process: {process_name}, Memory: {memory_usage:.2f} MB"
        )
    window.after(1000, update_process)

update_network_speed()
update_process()
        
window.mainloop()