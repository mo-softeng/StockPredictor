import requests, json, datetime


company = input("enter Ticker: ").lower()
start = datetime.date(2014,1,1)

headers = {
    'Content-Type': 'application/json',
}

with open("./config.json") as config:
    config = json.load(config)
    API_TOKEN = config["api_key"]
    
try: 
    requestResponse = requests.get(f"https://api.tiingo.com/tiingo/daily/{company}/prices?token={API_TOKEN}&startDate={start}", headers=headers)
    with open(F"./stock_data.json", "w") as stock_data:
        json.dump(requestResponse.json(), stock_data)
        print("retreived data")
except:
    print(f"Invalid ticker and or {requestResponse.status_code}")

