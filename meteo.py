import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("La clé n'a pas pu être récupérée dans le .env.")
    exit(1)


def getTemperature(ville):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ville}&appid={API_KEY}&units=metric&lang=fr"

    reponse = requests.get(url)
    if not reponse:
        print(f"{ville} n'existe pas ou est mal ecrite.")
        exit(1)
    donnees = reponse.json()

    return donnees

ville = input("Entrez une ville : ")

print(getTemperature(ville))