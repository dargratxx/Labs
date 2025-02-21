import requests

# пример api для погоды
api_url = "https://api.example.com/weather"

# параметры для запроса: город и api ключ (если нужен)
params = {
    "city": "New York",
    "apikey": "your_api_key_here"
}

# отправляем get-запрос к api
response = requests.get(api_url, params=params)

# проверяем, успешен ли запрос
if response.status_code == 200:
    weather_data = response.json()   # преобразуем json в словарь
    print("текущие данные о погоде:")
    print(weather_data)
else:
    print("не удалось получить данные. код статуса:", response.status_code)