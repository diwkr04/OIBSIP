pip install requests
import requests

def fetch_weath(api_key, locn):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": locn, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)

    if (response.status_code == 200):
        weath_data = response.json()
        return weath_data
    else:
        return None

def disp_weath(weath_data):
    if weath_data:
        temp = weath_data["main"]["temp"]
        humidity = weath_data["main"]["humidity"]
        weath_conds = weath_data["weather"][0]["description"]

        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Conditions: {weath_conds}")
    else:
        print("Unable to fetch weather data.")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    locn = input("Enter city or zip code: ")

    weath_data = get_weath(api_key, locn)

    disp_weath(weath_data)
   
