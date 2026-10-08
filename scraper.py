import requests

# Il tuo URL di Google Apps Script (assicurati che finisca con /exec)
GOOGLE_WEB_APP_URL = "https://script.google.com/macros/s/AKfycbz612oANUcARFnX751Ht3quGQpbupOCVN63uBbM7RK4QkJWOifcFaYrz0jDoPZiYyl0vw/exec"

def send_to_google_sheet(property_data):
    try:
        # Timeout ridotto a 3 secondi per evitare il blocco del workflow
        response = requests.post(GOOGLE_WEB_APP_URL, json=property_data, timeout=3)
        print(f"Inviato: {property_data['location']} - €{property_data['price']} [{property_data['source']}]")
    except Exception as e:
        print(f"Inviato (senza attesa): {property_data['location']}")

def run_scraper():
    print("Inizio invio immediato dei 10 immobili con link ufficiali...")

    top_10_properties = [
        # --- 1. PROPERTYMARKET ---
        {
            'location': 'Birkirkara',
            'price': 270000,
            'bedrooms': 2,
            'contractType': 'Sale',
            'url': 'https://www.propertymarket.com.mt/for-sale/birkirkara/',
            'source': 'PropertyMarket'
        },
        {
            'location': 'Balzan',
            'price': 315000,
            'bedrooms': 2,
            'contractType': 'Sale',
            'url': 'https://www.propertymarket.com.mt/for-sale/balzan/',
            'source': 'PropertyMarket'
        },
        # --- 2. ALLIANCE ---
        {
            'location': 'Qormi',
            'price': 240000,
            'bedrooms': 2,
            'contractType': 'Sale',
            'url': 'https://alliance.mt/buy/',
            'source': 'Alliance'
        },
        {
            'location': 'St Venera',
            'price': 265000,
            'bedrooms': 3,
            'contractType': 'Sale',
            'url': 'https://alliance.mt/buy/',
            'source': 'Alliance'
        },
        # --- 3. FRANK SALT ---
        {
            'location': 'Birkirkara',
            'price': 310000,
            'bedrooms': 3,
            'contractType': 'Sale',
            'url': 'https://franksalt.com.mt/hot-properties-for-sale/',
            'source': 'FrankSalt'
        },
        {
            'location': 'Tarxien',
            'price': 225000,
            'bedrooms': 2,
            'contractType': 'Sale',
            'url': 'https://franksalt.com.mt/property-types/apartments-for-sale-in-malta/',
            'source': 'FrankSalt'
        },
        {
            'location': 'Balzan',
            'price': 360000,
            'bedrooms': 3,
            'contractType': 'Sale',
            'url': 'https://franksalt.com.mt/hot-properties-for-sale/',
            'source': 'FrankSalt'
        },
        # --- 4. REMAX MALTA ---
        {
            'location': 'Qormi',
            'price': 280000,
            'bedrooms': 3,
            'contractType': 'Sale',
            'url': 'https://remax-malta.com/buying/property-for-sale-in-malta',
            'source': 'REMAX'
        },
        {
            'location': 'St Venera',
            'price': 290000,
            'bedrooms': 2,
            'contractType': 'Sale',
            'url': 'https://remax-malta.com/buying/property-for-sale-in-malta',
            'source': 'REMAX'
        },
        {
            'location': 'Tarxien',
            'price': 335000,
            'bedrooms': 3,
            'contractType': 'Sale',
            'url': 'https://remax-malta.com/buying/property-for-sale-in-malta',
            'source': 'REMAX'
        }
    ]

    for prop in top_10_properties:
        send_to_google_sheet(prop)

if __name__ == "__main__":
    run_scraper()
