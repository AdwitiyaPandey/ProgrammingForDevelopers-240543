import tkinter as tk
import threading
import time

BG = "#1e1e1e"
CARD = "#2b2b2b"
TEXT = "#ffffff"
ACCENT = "#4cc9f0"

root = tk.Tk()
root.title("Multi-threaded Weather Data Collector")
root.geometry("650x500")
root.configure(bg=BG)

title = tk.Label(root, text="Weather Kasto Hola", bg=BG, fg=ACCENT, font=("Segoe UI", 18, "bold"))
title.pack(pady=10)

control_frame = tk.Frame(root, bg=CARD, padx=20, pady=15)
control_frame.pack(pady=10, fill="x", padx=20)

tk.Label(control_frame, text="Locations:", bg=CARD, fg=TEXT).grid(row=0, column=0, sticky="w")

cities = ["Kathmandu", "Pokhara", "Chitwan", "Mardi Himal", "Lalitpur"]

city_text = tk.Label(control_frame, text=", ".join(cities), bg=CARD, fg="#bbbbbb")
city_text.grid(row=0, column=1, sticky="w")

button_frame = tk.Frame(root, bg=BG)
button_frame.pack(pady=10)

result_frame = tk.Frame(root, bg=CARD, padx=15, pady=15)
result_frame.pack(pady=10, fill="both", expand=True, padx=20)

tk.Label(result_frame, text="Weather Results", bg=CARD, fg=TEXT, font=("Segoe UI", 12, "bold")).pack(anchor="w")

result_text = tk.Text(result_frame, bg="#121212", fg=TEXT, insertbackground=TEXT, relief="flat", height=12)
result_text.pack(fill="both", expand=True, pady=10)

latency_frame = tk.Frame(root, bg=CARD, padx=15, pady=10)
latency_frame.pack(pady=10, fill="x", padx=20)

tk.Label(latency_frame, text="Sequential Time:", bg=CARD, fg=TEXT).grid(row=0, column=0, sticky="w")
seq_time_label = tk.Label(latency_frame, text="--", bg=CARD, fg=ACCENT)
seq_time_label.grid(row=0, column=1, sticky="w", padx=10)

tk.Label(latency_frame, text="Multithread Time:", bg=CARD, fg=TEXT).grid(row=1, column=0, sticky="w")
multi_time_label = tk.Label(latency_frame, text="--", bg=CARD, fg=ACCENT)
multi_time_label.grid(row=1, column=1, sticky="w", padx=10)

tk.Label(latency_frame, text="Speed Improvement:", bg=CARD, fg=TEXT).grid(row=2, column=0, sticky="w")
speed_label = tk.Label(latency_frame, text="--", bg=CARD, fg=ACCENT)
speed_label.grid(row=2, column=1, sticky="w", padx=10)


def fetch_weather(city):
    time.sleep(1)  
    return f"{city}: 25°C, Clear sky\n"



def fetch_sequential():
    result_text.delete("1.0", tk.END)
    start = time.time()

    for city in cities:
        data = fetch_weather(city)
        result_text.insert(tk.END, data)

    total = time.time() - start
    seq_time_label.config(text=f"{total:.2f} sec")



def fetch_multithreaded():
    result_text.delete("1.0", tk.END)
    start = time.time()
    results = []

    def worker(city):
        data = fetch_weather(city)
        results.append(data)

    threads = []
    for city in cities:
        t = threading.Thread(target=worker, args=(city,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    for r in results:
        result_text.insert(tk.END, r)

    total = time.time() - start
    multi_time_label.config(text=f"{total:.2f} sec")


# Comparison
def compare_performance():
    try:
        seq = float(seq_time_label.cget("text").split()[0])
        multi = float(multi_time_label.cget("text").split()[0])
        improvement = seq / multi
        speed_label.config(text=f"{improvement:.2f}x faster")
    except:
        speed_label.config(text="Run both first")



tk.Button(button_frame, text="Fetch Sequential", command=fetch_sequential,
          bg=ACCENT, fg="black", font=("Segoe UI", 10, "bold"),
          relief="flat", padx=15, pady=5).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="Fetch Multi-threaded", command=fetch_multithreaded,
          bg=ACCENT, fg="black", font=("Segoe UI", 10, "bold"),
          relief="flat", padx=15, pady=5).grid(row=0, column=1, padx=10)

tk.Button(button_frame, text="Compare Performance", command=compare_performance,
          bg=ACCENT, fg="black", font=("Segoe UI", 10, "bold"),
          relief="flat", padx=15, pady=5).grid(row=0, column=2, padx=10)

root.mainloop()

