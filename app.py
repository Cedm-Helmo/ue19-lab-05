import requests
import sys

API_URL = ('https://api.gemini.com/v2/ticker/btcusd')

try:
    r = requests.get(API_URL)
    r.status_code
    r.headers['content-type']
    r.encoding
    r.text
    data = r.json()

    Symbol = data.get('symbol')
    Open = data.get('open')
    high = data.get('high')
    low = data.get('low')
    close = data.get('close')

    print(f"Le prix de l'actif financier {Symbol} est actuellement à {close}$. Il a ouvert à {Open}$, a atteint un plus "
          f"haut de {high}$ et un plus bas de {low}$ aujourd'hui.")
except:
    print("Impossible de charger l'api")