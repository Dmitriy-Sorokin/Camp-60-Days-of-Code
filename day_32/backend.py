import requests

API_KEY = "349a35d3f3c95904257d35da7e26381d"


def get_data(place, forecast_day=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q=Minsk&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    print(data)
    return data


if __name__ == "__main__":
    get_data(place="Minsk")
