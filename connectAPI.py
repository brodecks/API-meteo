import requests
from dotenv import load_dotenv
import os
from datetime import datetime


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

    heure_mesure = datetime.fromtimestamp(donnees['dt']).strftime('%H:%M:%S')
    print(f"Données relevées à : {heure_mesure}")

    villeInput = donnees['name']
    tempVille = donnees['main']['temp']
    tempsCiel = donnees['weather'][0]['description']

    tabVille = {
        'ville': villeInput,
        'temperature': tempVille,
        'temps_dehors': tempsCiel
    }

    return tabVille
