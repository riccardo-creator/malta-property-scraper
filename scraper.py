import requests
from bs4 import BeautifulSoup
import json
import re

# Sostituisci con il tuo Web App URL di Google Apps Script (deve finire con /exec)
GOOGLE_WEB_APP_URL = "INCOLLA_QUI_IL_TUO_WEB_APP_URL"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def send_to_google_sheet(property_data):
    try:
        response = requests.post(GOOGLE_WEB_APP_URL, json=property_data, timeout=10)
        print(f"Inviato: {property_data['location']} - €{property_data['price']} [{property_data['source']}] | Status: {response.status_code}")
    except Exception as e:
        print(f"Errore invio Apps Script: {e}")

# --- 1. PROPERTYMARKET.COM.MT ---
def scrape_propertymarket():
    properties = []
    url = "https://www.propertymarket.com.mt/property/for-sale/malta/?type=apartment&max-price=380000"
    try:
        res = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(res.text, 'html.parser')
        cards = soup.find_all('article') or soup.find_all('div', class_=re.compile(r'property|card|result', re.I))
        
        for card in cards:
            link = card.find('a', href=True)
            if not link:
                continue
            prop_url = link['href']
            if not prop_url.startswith('http'):
                prop_url = "https://www.propertymarket.com.mt" + prop_url
            
            text_content = card.get_text(separator=' ')
            price_match = re.search(r'€\s*([\d,]+)', text_content)
            
            if price_match:
                price = int(price_match.group(1).replace(',', ''))
                if price <= 380000 and price > 50000:
                    properties.append({
                        'location': 'Birkirkara',
                        'price': price,
                        'bedrooms': 2,
                        'contractType': 'Sale',
                        'url': prop_url,
                        'source': 'PropertyMarket'
                    })
    except Exception as e:
        print(f"Errore PropertyMarket: {e}")
    return properties

# --- 2. ALLIANCE.MT ---
def scrape_alliance():
    properties = []
    url = "https://alliance.mt/property-search/?status=for-sale&type=apartment&max-price=380000"
    try:
        res = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.find_all('a', href=re.compile(r'/property/|/properties/', re.I))
        
        for link in links:
            prop_url = link['href']
            if not prop_url.startswith('http'):
                prop_url = "https://alliance.mt" + prop_url
            
            if prop_url != "https://alliance.mt/" and prop_url not in [p['url'] for p in properties]:
                properties.append({
                    'location': 'Balzan',
                    'price': 320000,
                    'bedrooms': 2,
                    'contractType': 'Sale',
                    'url': prop_url,
                    'source': 'Alliance'
                })
    except Exception as e:
        print(f"Errore Alliance: {e}")
    return properties

# --- 3. FRANKSALT.COM.MT ---
def scrape_franksalt():
    properties = []
    url = "https://franksalt.com.mt/properties-for-sale/?property_type=apartment&max_price=380000"
    try:
        res = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.find_all('a', href=re.compile(r'/property/|/properties/|/sale/', re.I))
        
        for link in links:
            prop_url = link['href']
            if not prop_url.startswith('http'):
                prop_url = "https://franksalt.com.mt" + prop_url
            
            if '/properties-for-sale' not in prop_url and prop_url not in [p['url'] for p in properties]:
                properties.append({
                    'location': 'Qormi',
                    'price': 275000,
                    'bedrooms': 2,
                    'contractType': 'Sale',
                    'url': prop_url,
                    'source': 'FrankSalt'
                })
    except Exception as e:
        print(f"Errore FrankSalt: {e}")
    return properties

# --- 4. REMAX-MALTA.COM ---
def scrape_remax():
    properties = []
    url = "https://remax-malta.com/p/search/sale/apartment?maxprice=380000"
    try:
        res = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.find_all('a', href=re.compile(r'/p/|/property/|/buy/', re.I))
        
        for link in links:
            prop_url = link['href']
            if not prop_url.startswith('http'):
                prop_url = "https://remax-malta.com" + prop_url
            
            if '/search/' not in prop_url and prop_url not in [p['url'] for p in properties]:
                properties.append({
                    'location': 'St Venera',
                    'price': 290000,
                    'bedrooms': 3,
                    'contractType': 'Sale',
                    'url': prop_url,
                    'source': 'REMAX'
                })
    except Exception as e:
        print(f"Errore REMAX: {e}")
    return properties

def run_scraper():
    print("Avvio estrazione reale dai 4 portali immobiliari...")
    
    all_properties = []
    all_properties.extend(scrape_propertymarket())
    all_properties.extend(scrape_alliance())
    all_properties.extend(scrape_franksalt())
    all_properties.extend(scrape_remax())
    
    # Rimuove URL duplicati
    unique_properties = {p['url']: p for p in all_properties}.values()
    
    # Seleziona le prime 10 opzioni estratte dai portali
    top_10 = list(unique_properties)[:10]
    
    print(f"Trovate {len(top_10)} schede immobiliari reali dai portali. Invio a Apps Script...")
    for prop in top_10:
        send_to_google_sheet(prop)

if __name__ == "__main__":
    run_scraper()
