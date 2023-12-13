import requests
import json


url = "https://eu.charge.mercedes.me/api/map/v1/de/query"

request_data = {
    "DCSChargePointDynStatusRequest": [
        {"dcsChargePointId": "DE:DCS:CHARGE_POINT:1018e070-9e00-39e1-aea4-e141b586ee39"},
        {"dcsChargePointId": "DE:DCS:CHARGE_POINT:41982817-d384-322b-b09b-3f46875d594b"},
        {"dcsChargePointId": "DE:DCS:CHARGE_POINT:ac7f695e-be18-37b9-83ce-f00c189e8add"},
        {"dcsChargePointId": "DE:DCS:CHARGE_POINT:f87a9bf2-e29f-343e-b80b-ac949c239e2b"}
    ]
}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Origin": "https://eu.charge.mercedes.me",
    "Connection": "keep-alive",
    "Referer": "https://eu.charge.mercedes.me/web/daimler-de/map",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "rest-api-path": "charge-points"  
}

try:
    # Deaktiviere SSL-Überprüfung vorübergehend
    response = requests.post(url, json=request_data, headers=headers, verify=False)
    response.raise_for_status()  # Raises HTTPError for bad responses
except requests.exceptions.RequestException as e:
    print(f"Fehler bei der Anfrage: {e}")
else:
    if response.ok:
        print(response.json())
    else:
        print(f"Fehler bei der Anfrage. Statuscode: {response.status_code}")
