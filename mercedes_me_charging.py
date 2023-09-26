import requests
import json

# Die URL der API-Endpunkt
url = "https://eu.charge.mercedes.me/o/dcs-api/map/query/post?groupId=38295"

# JSON-Daten für den POST-Request (basierend auf Ihrem Request)
request_data = {
    "DCSChargePointDynStatusRequest": [
        {"dcsChargePointId": "DE:DCS:CHARGE_POINT:1018e070-9e00-39e1-aea4-e141b586ee39"},
        {"dcsChargePointId": "DE:DCS:CHARGE_POINT:41982817-d384-322b-b09b-3f46875d594b"},
        {"dcsChargePointId": "DE:DCS:CHARGE_POINT:ac7f695e-be18-37b9-83ce-f00c189e8add"},
        {"dcsChargePointId": "DE:DCS:CHARGE_POINT:f87a9bf2-e29f-343e-b80b-ac949c239e2b"}
    ]
}

# Header für die POST-Anfrage (basierend auf Ihrem Beispiel)
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "Content-Length": str(len(json.dumps(request_data))),
    "Origin": "https://eu.charge.mercedes.me",
    "Connection": "keep-alive",
    "Referer": "https://eu.charge.mercedes.me/web/daimler-de/map",
    "Cookie": "JSESSIONID=C8E9D5B2AB604AF2658B86EF250D543E.n1; CN_ALLOW_FUNCTIONAL_COOKIES=true; COOKIE_SUPPORT=true; GUEST_LANGUAGE_ID=de_DE; mp_45d34ff2107c23df37a32df803d40170_mixpanel=%7B%22distinct_id%22%3A%20%2218ad25e592f27d-06224e9126d57a-9762631-ff000-18ad25e593025%22%2C%22%24device_id%22%3A%20%2218ad25e592f27d-06224e9126d57a-9762631-ff000-18ad25e593025%22%2C%22%24user_id%22%3A%20%2218ad25e592f27d-06224e9126d57a-9762631-ff000-18ad25e593025%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22User%20Agent%22%3A%20%22Mozilla%2F5.0%20(X11%3B%20Ubuntu%3B%20Linux%20x86_64%3B%20rv%3A109.0)%20Gecko%2F20100101%20Firefox%2F117.0%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22oem%22%3A%20%22DAIMLER%22%2C%22lastEventTime%22%3A%201695746515996%2C%22sessionId%22%3A%20%22274d7dea-6bb9-3b16-9d33-11765ad37176%22%7D",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "rest-api-path": "charge-points"  # Fügen Sie den rest-api-path Header hinzu
}

# Führen Sie die POST-Anfrage an die API durch
response = requests.post(url, json=request_data, headers=headers)

# Überprüfen Sie den Statuscode der Antwort
if response.status_code == 200:
    # Die Antwort wurde erfolgreich empfangen
    # Drucken Sie den Inhalt der Antwort
    print(response.json())
else:
    # Bei einem Fehler den Statuscode anzeigen
    print(f"Fehler bei der Anfrage. Statuscode: {response.status_code}")
