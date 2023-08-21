import requests

API_KEY = "349a35d3f3c95904257d35da7e26381d"


def get_data(place, forecast_day=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    filtered_data = data["list"]
    nr_value = 8 * forecast_day
    filtered_data = filtered_data[:nr_value]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Minsk", forecast_day=3))
