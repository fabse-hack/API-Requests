import requests

# Liste der Geräte-IDs, die du abfragen möchtest
device_ids = [1005629165, 1005954355, 1005954365]  # Füge hier die gewünschten IDs hinzu

# Basis-URL der API
base_url = "https://mc.chargepoint.com/map-prod/v3/station/info"

# Leerer Dictionary, um die Ergebnisse zu speichern
sensor_data = {}

# Schleife durch die Liste der Geräte-IDs
for device_id in device_ids:
    # Erstelle die vollständige URL für die Abfrage
    url = f"{base_url}?deviceId={device_id}"
    
    # Führe die GET-Anfrage durch
    response = requests.get(url)
    
    # Überprüfe, ob die Anfrage erfolgreich war (Statuscode 200)
    if response.status_code == 200:
        # Lese die JSON-Daten aus der Antwort
        data = response.json()
        
        # Speichere die Daten im Dictionary mit der Geräte-ID als Schlüssel
        sensor_data[device_id] = data
    else:
        print(f"Fehler bei der Abfrage der Geräte-ID {device_id}")

# Jetzt kannst du auf die Sensor-Daten für jede Geräte-ID zugreifen
for device_id, data in sensor_data.items():
    print(f"Sensor-Daten für Geräte-ID {device_id}:")
    print(data)
