import requests

def fetch_data_from_api():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data= response.json()
    if data["success"] and "data" in data:
        userdata = data["data"]
        testuser = userdata["login"]["username"]
        testpassword = userdata["login"]["password"]
        country = userdata["location"]["country"]
        return testuser, testpassword, country
    else:
        raise Exception("Failed to fetch data from API")

def user():
    try:
        testuser, testpassword, country = fetch_data_from_api()
        print(f"Username: {testuser}")
        print(f"Password: {testpassword}")
        print(f"Country: {country}")
    except Exception as e:
        print(str(e))

        
if __name__ == "__main__":
    user()    