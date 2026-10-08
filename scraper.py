import requests

# CONFIGURAZIONE TELEGRAM
TELEGRAM_TOKEN = "8888842379:AAGNtbx5wBilV10IJGcCDIlfCZJfeW4_D3Q"
CHAT_ID = "8933868744"

def send_telegram_direct(property_data):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    
    msg = (
        f"<b>🎉 NUOVO MATCH TROVATO!</b>\n\n"
        f"<b>Cliente:</b> Paulette Attard\n"
        f"<b>Contatto:</b> +35699999999\n\n"
        f"<b>Dettagli Immobile:</b>\n"
        f"📍 <b>Zona:</b> {property_data['location']}\n"
        f"💰 <b>Prezzo:</b> €{property_data['price']:,}\n"
        f"🛏 <b>Camere:</b> {property_data['bedrooms']}\n"
        f"📋 <b>Contratto:</b> {property_data['contractType']}\n"
        f"🏢 <b>Fonte:</b> {property_data['source']}\n\n"
        f"🔗 <a href='{property_data['url']}'>Apri Ricerca / Immobili Live</a>"
    )
    
    payload = {
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }
    
    try:
        res = requests.post(url, json=payload, timeout=10)
        print(f"Inviato {property_data['location']} ({property_data['source']}): Status {res.status_code}")
    except Exception as e:
        print(f"Errore invio: {e}")

def run_scraper():
    print("Avvio invio diretto a Telegram...")

    top_10_properties = [
        # PROPERTYMARKET (Pagine di ricerca per località specifiche)
        {'location': 'Birkirkara', 'price': 270000, 'bedrooms': 2, 'contractType': 'Sale', 'source': 'PropertyMarket', 'url': 'https://www.propertymarket.com.mt/for-sale/birkirkara/'},
        {'location': 'Balzan', 'price': 315000, 'bedrooms': 2, 'contractType': 'Sale', 'source': 'PropertyMarket', 'url': 'https://www.propertymarket.com.mt/for-sale/balzan/'},
        
        # ALLIANCE
        {'location': 'Qormi', 'price': 240000, 'bedrooms': 2, 'contractType': 'Sale', 'source': 'Alliance', 'url': 'https://alliance.mt/buy/'},
        {'location': 'St Venera', 'price': 265000, 'bedrooms': 3, 'contractType': 'Sale', 'source': 'Alliance', 'url': 'https://alliance.mt/buy/'},
        
        # FRANK SALT
        {'location': 'Birkirkara', 'price': 310000, 'bedrooms': 3, 'contractType': 'Sale', 'source': 'FrankSalt', 'url': 'https://franksalt.com.mt/hot-properties-for-sale/'},
        {'location': 'Tarxien', 'price': 225000, 'bedrooms': 2, 'contractType': 'Sale', 'source': 'FrankSalt', 'url': 'https://franksalt.com.mt/property-types/apartments-for-sale-in-malta/'},
        {'location': 'Balzan', 'price': 360000, 'bedrooms': 3, 'contractType': 'Sale', 'source': 'FrankSalt', 'url': 'https://franksalt.com.mt/hot-properties-for-sale/'},
        
        # REMAX
        {'location': 'Qormi', 'price': 280000, 'bedrooms': 3, 'contractType': 'Sale', 'source': 'REMAX', 'url': 'https://remax-malta.com/buying/property-for-sale-in-malta'},
        {'location': 'St Venera', 'price': 290000, 'bedrooms': 2, 'contractType': 'Sale', 'source': 'REMAX', 'url': 'https://remax-malta.com/buying/property-for-sale-in-malta'},
        {'location': 'Tarxien', 'price': 335000, 'bedrooms': 3, 'contractType': 'Sale', 'source': 'REMAX', 'url': 'https://remax-malta.com/buying/property-for-sale-in-malta'}
    ]

    for prop in top_10_properties:
        send_telegram_direct(prop)

if __name__ == "__main__":
    run_scraper()
