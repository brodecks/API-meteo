import tkinter as tk
from connectAPI import getTemperature


ville = input("Entrez le nom de la ville : ")

data = getTemperature(ville)

print(f"A {data['ville']}, il fait {data['temperature']} degrès, et voici le temps de dehors : {data['temps_dehors']}.")

#creer page d'accueil avec champ de saisi d'une ville
