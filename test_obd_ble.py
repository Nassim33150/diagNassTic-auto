import asyncio
from bleak import BleakScanner

async def scan_ble_devices():
    print("Recherche des périphériques BLE...")
    
    devices = await BleakScanner.discover()  # Scan des périphériques
    
    if devices:
        print("\n📡 Périphériques détectés :")
        for device in devices:
            print(f"🔹 Nom: {device.name}, Adresse: {device.address}, RSSI: {device.rssi} dBm")
    else:
        print("❌ Aucun périphérique BLE trouvé.")

# Exécuter l'événement async
asyncio.run(scan_ble_devices())
