from connectAPI import getTemperature
import tkinter as tk


ville = input("Entrez le nom de la ville : ")

data = getTemperature(ville)

print(f"A {data['ville']}, il fait {data['temperature']} degrès.")
if 'nuageux' in data['temps_dehors']:
    print("Le temps de dehors est nuageux.")
elif 'couvert' in data['temps_dehors']:
    print("Le temps de dehors est couvert.")
#coder interface avec tableau de chaque temps