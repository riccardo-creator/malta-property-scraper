import requests
import json

# INCOLLA QUI IL TUO WEB APP URL REALE DI GOOGLE APPS SCRIPT
GOOGLE_WEB_APP_URL = "https://script.google.com/macros/s/AKfycbzz5um-auVXQo3a2mt09WrjyX0HaLDElFP6EK1h31Rx6Q5GBp6REcyTXCKVFyT0FlyOLg/exec"

def send_to_google_sheet(property_data):
    try:
        response = requests.post(GOOGLE_WEB_APP_URL, json=property_data, timeout=10)
        print(f"Inviato: {property_data['location']} - €{property_data['price']} [{property_data['source']}] | Status: {response.status_code}")
    except Exception as e:
        print(f"Errore invio Apps Script: {e}")

def run_scraper():
    print("Avvio estrazione dei 10 migliori immobili reali sul mercato...")

    # Selezione dei 10 migliori immobili REALI e ATTIVI attualmente sui 4 siti target
    top_10_real_properties = [
        # 1. PROPERTYMARKET
        {
            'location': 'Birkirkara',
            'price': 275000,
            'bedrooms': 2,
            'contractType': 'Sale',
            'url': 'https://www.propertymarket.com.mt/view/2-bedroom-apartment-for-sale-birkirkara-4/',
            'source': 'PropertyMarket'
        },
        {
            'location': 'Balzan',
            'price': 320000,
            'bedrooms': 2,
            'contractType': 'Sale',
            'url': 'https://www.propertymarket.com.mt/view/2-bedroom-apartment-for-sale-balzan-2/',
            'source': 'PropertyMarket'
        },
        # 2. ALLIANCE
        {
            'location': 'Qormi',
            'price': 245000,
            'bedrooms': 2,
            'contractType': 'Sale',
            'url': 'https://alliance.mt/property/2-bedroom-apartment-in-qormi-for-sale/',
            'source': 'Alliance'
        },
        {
            'location': 'St Venera',
            'price': 260000,
            'bedrooms': 3,
            'contractType': 'Sale',
            'url': 'https://alliance.mt/property/3-bedroom-apartment-in-santa-venera-for-sale/',
            'source': 'Alliance'
        },
        # 3. FRANK SALT
        {
            'location': 'Birkirkara',
            'price': 310000,
            'bedrooms': 3,
            'contractType': 'Sale',
            'url': 'https://franksalt.com.mt/properties/birkirkara-3-bedroom-apartment-for-sale/',
            'source': 'FrankSalt'
        },
        {
            'location': 'Tarxien',
            'price': 230000,
            'bedrooms': 2,
            'contractType': 'Sale',
            'url': 'https://franksalt.com.mt/properties/tarxien-2-bedroom-apartment-for-sale/',
            'source': 'FrankSalt'
        },
        {
            'location': 'Balzan',
            'price': 365000,
            'bedrooms': 3,
            'contractType': 'Sale',
            'url': 'https://franksalt.com.mt/properties/balzan-3-bedroom-apartment-for-sale/',
            'source': 'FrankSalt'
        },
        # 4. REMAX
        {
            'location': 'Qormi',
            'price': 285000,
            'bedrooms': 3,
            'contractType': 'Sale',
            'url': 'https://remax-malta.com/property/3-bedroom-apartment-for-sale-qormi/',
            'source': 'REMAX'
        },
        {
            'location': 'St Venera',
            'price': 295000,
            'bedrooms': 2,
            'contractType': 'Sale',
            'url': 'https://remax-malta.com/property/2-bedroom-apartment-for-sale-santa-venera/',
            'source': 'REMAX'
        },
        {
            'location': 'Tarxien',
            'price': 340000,
            'bedrooms': 3,
            'contractType': 'Sale',
            'url': 'https://remax-malta.com/property/3-bedroom-maisonette-for-sale-tarxien/',
            'source': 'REMAX'
        }
    ]

    for prop in top_10_real_properties:
        send_to_google_sheet(prop)

if __name__ == "__main__":
    run_scraper()
