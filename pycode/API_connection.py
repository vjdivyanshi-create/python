import requests

def weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b708573c6bece6c509e24bd3ce541296&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"weather data for:{city}")
        for i in range(6):
            for key, value in data['main'].items():
                print(f"{key}: {value}")
    except requests.exceptions.RequestException as e:
        print(e)


city = input("enter city name:")
weather_data(city)