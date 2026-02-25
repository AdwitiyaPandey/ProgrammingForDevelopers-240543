import tkinter as tk
from tkinter import messagebox

# data for tourist spots in Kathmandu
spots = [
    {"name": "Pashupatinath", "cost": 1000, "time": 2, "interest": 9, "distance": 3},
    {"name": "Boudhanath", "cost": 800, "time": 1.5, "interest": 8, "distance": 4},
    {"name": "Swayambhunath", "cost": 500, "time": 2, "interest": 9, "distance": 5},
    {"name": "Durbar Square", "cost": 1200, "time": 2.5, "interest": 8, "distance": 2},
    {"name": "Garden of Dreams", "cost": 400, "time": 1, "interest": 7, "distance": 1},
    {"name": "Thamel", "cost": 0, "time": 3, "interest": 6, "distance": 2},
    {"name": "Patan Durbar Square", "cost": 1000, "time": 2, "interest": 8, "distance": 4},
    {"name": "Bhaktapur Durbar Square", "cost": 900, "time": 2, "interest": 8, "distance": 6},
]


def greedy_itinerary(budget, time_limit):
    selected = []
    total_cost = 0
    total_time = 0

    sorted_spots = sorted(
        spots,
        key=lambda s: (s["interest"] * 2 - s["cost"] * 0.002 - s["time"] * 0.5 - s["distance"] * 0.3),
        reverse=True
    )

    for spot in sorted_spots:
        if total_cost + spot["cost"] <= budget and total_time + spot["time"] <= time_limit:
            selected.append(spot)
            total_cost += spot["cost"]
            total_time += spot["time"]

    return selected, total_cost, total_time

def plan_trip():
    try:
        budget = float(budget_entry.get())
        time_limit = float(time_entry.get())

        route, cost, time_used = greedy_itinerary(budget, time_limit)

        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Recommended Itinerary\n\n")

        for place in route:
            result_text.insert(tk.END, f"• {place['name']}\n")

        result_text.insert(tk.END, f"\nTotal Cost: {cost}")
        result_text.insert(tk.END, f"\nTotal Time: {time_used} hrs")

        result_text.insert(tk.END, "\n\nDecision Strategy:\n")
        result_text.insert(tk.END, "Greedy selection based on interest, cost, time, and distance.")

    except:
        messagebox.showerror("Error", "Enter valid numbers")


BG = "#1e1e1e"
CARD = "#2b2b2b"
TEXT = "#ffffff"
INPUT = "#3a3a3a"
ACCENT = "#4cc9f0"

root = tk.Tk()
root.title("Tourist Spot Optimizer")
root.geometry("520x460")
root.configure(bg=BG)

title = tk.Label(root, text="Tourist Spot Optimizer", bg=BG, fg=ACCENT, font=("Segoe UI", 15, "bold"))
title.pack(pady=10)

form = tk.Frame(root, bg=CARD, padx=20, pady=15)
form.pack(pady=10)

tk.Label(form, text="Budget:", bg=CARD, fg=TEXT).pack(anchor="w")
budget_entry = tk.Entry(form, bg=INPUT, fg=TEXT, insertbackground=TEXT, relief="flat")
budget_entry.pack(fill="x", pady=5)

tk.Label(form, text="Available Time (hours):", bg=CARD, fg=TEXT).pack(anchor="w")
time_entry = tk.Entry(form, bg=INPUT, fg=TEXT, insertbackground=TEXT, relief="flat")
time_entry.pack(fill="x", pady=5)

tk.Button(
    root,
    text="Generate Itinerary",
    command=plan_trip,
    bg=ACCENT,
    fg="black",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=10,
    pady=5
).pack(pady=10)

result_text = tk.Text(
    root,
    height=14,
    width=58,
    bg="#121212",
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat"
)
result_text.pack(pady=10)

root.mainloop()
