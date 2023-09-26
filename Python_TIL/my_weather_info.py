import requests
import json

def get_weather_info(city, apikey="3d49dc3f03d7cf4092cca0aacd67efc7", lang="kr"):
    api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric'
    response = requests.get(api)

    if response.status_code == 200:
        data = json.loads(response.text)
        weather = data["weather"][0]["main"]
        temp = data["main"]["temp"]
        return weather, temp
    else:
        print("요청 실패!")

if __name__ == "__main__":
    print(get_weather_info.__name__)
    city = "Seoul"
    weather, temp = get_weather_info(city)
    print(weather, temp)


def main(city, apikey="3d49dc3f03d7cf4092cca0aacd67efc7", lang="kr"):
    api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric'
    response = requests.get(api)

    if response.status_code == 200:
        data = json.loads(response.text)
        weather = data["weather"][0]["main"]
        temp = data["main"]["temp"]
        return weather, temp
    else:
        print("요청 실패!")

if __name__ == "__main__":
    print(main.__name__)
    city = "Seoul"
    weather, temp = main(city)
    print(weather, temp)