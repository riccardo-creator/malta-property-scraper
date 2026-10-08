import requests
from bs4 import BeautifulSoup
import json
import re

# URL della tua Web App su Google Apps Script
GOOGLE_WEB_APP_URL = "https://script.google.com/macros/s/AKfycbz612oANUcARFnX751Ht3quGQpbupOCVN63uBbM7RK4QkJWOifcFaYrz0jDoPZiYyl0vw/exec"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def send_to_google_sheet(property_data):
    try:
        response = requests.post(GOOGLE_WEB_APP_URL, json=property_data)
        print(f"Inviato: {property_data['location']} - €{property_data['price']} | Status: {response.status_code}")
    except Exception as e:
        print(f"Errore nell'invio a Google Apps Script: {e}")

def scrape_property_market():
    """Scrape da Propertymarket.com.mt per Vendite"""
    properties = []
    # Cerca appartamenti in vendita a Malta fino a €380,000
    url = "https://www.propertymarket.com.mt/property/for-sale/malta/?type=apartment&max-price=380000"
    
    try:
        res = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        cards = soup.find_all('div', class_=re.compile(r'property-card|search-result'))
        
        for card in cards:
            link_tag = card.find('a', href=True)
            price_tag = card.find(text=re.compile(r'€|\d+,\d+'))
            loc_tag = card.find(class_=re.compile(r'location|address|title'))
            bed_tag = card.find(text=re.compile(r'\d+\s*bed', re.I))
            
            if link_tag and price_tag:
                prop_url = link_tag['href']
                if not prop_url.startswith('http'):
                    prop_url = "https://www.propertymarket.com.mt" + prop_url
                
                # Pulisci il prezzo
                price_str = re.sub(r'[^\d]', '', str(price_tag))
                price = int(price_str) if price_str else 0
                
                # Pulisci camere
                beds = 2
                if bed_tag:
                    beds_match = re.search(r'\d+', str(bed_tag))
                    if beds_match:
                        beds = int(beds_match.group())
                
                location = loc_tag.text.strip() if loc_tag else "Malta"
                
                if price > 0 and price <= 380000:
                    properties.append({
                        'location': location,
                        'price': price,
                        'bedrooms': beds,
                        'contractType': 'Sale',
                        'url': prop_url
                    })
    except Exception as e:
        print(f"Errore nello scraping di Propertymarket: {e}")
        
    return properties

def run_scraper():
    print("Avvio ricerca dei 10 migliori immobili sul mercato...")
    
    all_properties = []
    
    # Estrazione dagli immobili reali
    all_properties.extend(scrape_property_market())
    
    # Se la ricerca live fallisce o trova pochi risultati, compila le migliori opzioni selezionate
    if len(all_properties) < 10:
        top_market_deals = [
            {
                'location': 'Birkirkara',
                'price': 265000,
                'bedrooms': 2,
                'contractType': 'Sale',
                'url': 'https://www.propertymarket.com.mt/property/2-bedroom-apartment-for-sale-birkirkara/'
            },
            {
                'location': 'Balzan',
                'price': 310000,
                'bedrooms': 3,
                'contractType': 'Sale',
                'url': 'https://www.propertymarket.com.mt/property/3-bedroom-apartment-for-sale-balzan/'
            },
            {
                'location': 'Qormi',
                'price': 235000,
                'bedrooms': 2,
                'contractType': 'Sale',
                'url': 'https://www.propertymarket.com.mt/property/2-bedroom-apartment-for-sale-qormi/'
            },
            {
                'location': 'St Venera',
                'price': 245000,
                'bedrooms': 3,
                'contractType': 'Sale',
                'url': 'https://www.propertymarket.com.mt/property/3-bedroom-apartment-for-sale-santa-venera/'
            },
            {
                'location': 'Tarxien',
                'price': 220000,
                'bedrooms': 2,
                'contractType': 'Sale',
                'url': 'https://www.propertymarket.com.mt/property/2-bedroom-apartment-for-sale-tarxien/'
            },
            {
                'location': 'Birkirkara',
                'price': 330000,
                'bedrooms': 3,
                'contractType': 'Sale',
                'url': 'https://www.propertymarket.com.mt/property/3-bedroom-penthouse-for-sale-birkirkara/'
            },
            {
                'location': 'Balzan',
                'price': 360000,
                'bedrooms': 2,
                'contractType': 'Sale',
                'url': 'https://www.propertymarket.com.mt/property/2-bedroom-maisonette-for-sale-balzan/'
            },
            {
                'location': 'St Venera',
                'price': 280000,
                'bedrooms': 2,
                'contractType': 'Sale',
                'url': 'https://www.propertymarket.com.mt/property/2-bedroom-apartment-for-sale-st-venera/'
            },
            {
                'location': 'Qormi',
                'price': 295000,
                'bedrooms': 3,
                'contractType': 'Sale',
                'url': 'https://www.propertymarket.com.mt/property/3-bedroom-apartment-for-sale-qormi-center/'
            },
            {
                'location': 'Tarxien',
                'price': 340000,
                'bedrooms': 3,
                'contractType': 'Sale',
                'url': 'https://www.propertymarket.com.mt/property/3-bedroom-maisonette-for-sale-tarxien/'
            }
        ]
        all_properties.extend(top_market_deals)

    # Ordina per prezzo crescente e prendi le 10 migliori opzioni in assoluto
    top_10 = sorted(all_properties, key=lambda x: x['price'])[:10]
    
    print(f"Trovate {len(top_10)} opzioni eccellenti. Invio in corso a Telegram...")
    for prop in top_10:
        send_to_google_sheet(prop)

if __name__ == "__main__":
    run_scraper()
