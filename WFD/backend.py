import requests

API_KEY = "cfd38b059b41f0a2938e91315fe06bfa"


def get_data(place, days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        filtered_data = data["list"]
        nr_values = 8 * days
        filtered_data = filtered_data[:nr_values]
    except KeyError:
        return "Wrong City"

    return filtered_data


if __name__ == "__main__":
    print(get_data("Mexico", 3))
