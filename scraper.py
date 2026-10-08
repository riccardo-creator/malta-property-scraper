import requests
from bs4 import BeautifulSoup
import json
import re

# URL della tua Web App Google Apps Script
GOOGLE_WEB_APP_URL = "https://script.google.com/macros/s/AKfycbz612oANUcARFnX751Ht3quGQpbupOCVN63uBbM7RK4QkJWOifcFaYrz0jDoPZiYyl0vw/exec"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

def send_to_google_sheet(property_data):
    try:
        response = requests.post(GOOGLE_WEB_APP_URL, json=property_data)
        print(f"Inviato: {property_data['location']} - €{property_data['price']} | Status: {response.status_code}")
    except Exception as e:
        print(f"Errore nell'invio dei dati: {e}")

# Esempio di funzione di scraping generica per i portali
def scrape_portals():
    print("Avvio scansione portali immobiliari Malta...")
    
    # Esempio di struttura di dati estratta (lo script analizzerà le schede)
    # Verranno scansionati propertymarket, alliance, franksalt e remax-malta
    sample_matches = [
        {
            'location': 'Birkirkara',
            'price': 350000,
            'bedrooms': 2,
            'contractType': 'Sale',
            'url': 'https://www.alliance.mt/'
        },
        {
            'location': 'St. Julian\'s',
            'price': 420000,
            'bedrooms': 3,
            'contractType': 'Sale',
            'url': 'https://alliance.mt/'
        }
    ]
    
    for item in sample_matches:
        send_to_google_sheet(item)

if __name__ == "__main__":
    scrape_portals()
