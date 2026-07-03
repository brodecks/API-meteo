from connectAPI import getTemperature
import tkinter as tk
import math


def show_sunny_sky(data):
    if 'nuageux' in data['temps_dehors'] or 'couvert' in data['temps_dehors']:
        return
    
    root = tk.Tk()
    root.title(f"Météo à {data['ville']}")
    
    canvas = tk.Canvas(root, width=400, height=300, bg='skyblue')
    canvas.pack()
    
    # Soleil
    canvas.create_oval(150, 50, 250, 150, fill='yellow', outline='orange', width=4)
    
    # Rayons du soleil
    for i in range(0, 360, 45):
        angle = math.radians(i)
        x = 200 + 80 * math.cos(angle)
        y = 100 + 80 * math.sin(angle)
        canvas.create_line(200, 100, x, y, fill='gold', width=3)
    
    # Température
    canvas.create_text(200, 200, text=f"{data['temperature']}°C", font=('Arial', 24, 'bold'), fill='white')
    canvas.create_text(200, 240, text=data['temps_dehors'].capitalize(), font=('Arial', 16), fill='white')
    
    root.mainloop()



ville = input("Entrez le nom de la ville : ")


data = getTemperature(ville)


print(f"A {data['ville']}, il fait {data['temperature']} degrès.")
if 'nuageux' in data['temps_dehors']:
    print("Le temps de dehors est nuageux.")
elif 'couvert' in data['temps_dehors']:
    print("Le temps de dehors est couvert.")

show_sunny_sky(data)