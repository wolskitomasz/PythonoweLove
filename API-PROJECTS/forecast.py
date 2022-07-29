import requests

Api_key = '84f7b06b31b3de6843a89f31d08c4502'
Base_url = 'https://api.openweathermap.org/data/2.5/weather'

city = input('Podaj miasto: ')
request_url = f'{Base_url}?q={city}&appid={Api_key}'

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 1)
    print(f'Status pogody: {weather}')
    print(f'Temperatura: {temperature} stopni Celcjusza.')
    
else:
    print('Błąd.')
    print(request_url)