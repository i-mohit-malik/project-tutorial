import requests
import random

def fetch_data_from_api2():
    url="https://api.freeapi.app/api/v1/public/stocks/"
    response = requests.get(url)
    data= response.json()
    if data["success"] and "data" in data:
        userdata = data["data"]["data"]
        x=random.randint(0,9)
        testfirm = userdata[x]["Name"]
        isin = userdata[x]["ISIN"]
        market = userdata[x]["MarketCap"]
        return testfirm, isin, market
    else:
        raise Exception("Failed to fetch data from API")

def firm():
    try:
        testfirm, isin, market = fetch_data_from_api2()
        print(f"Company: {testfirm}")
        print(f"ISIN: {isin}")
        print(f"Market Cap: {market}")
    except Exception as e:
        print(str(e))

        
if __name__ == "__main__":
    firm()    