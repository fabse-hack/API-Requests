import requests

def main():
    url = "https://mc.chargepoint.com/map-prod/v3/station/info?deviceId=1005954365"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Antwort von der URL:")
        print(response.text)
    else:
        print("Fehler beim Abrufen der URL. Statuscode:", response.status_code)

if __name__ == "__main__":
    main()
