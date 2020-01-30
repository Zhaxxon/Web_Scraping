from pprint import pprint
import requests
import json
#e5e4cd692a72b0b66ea0a6b80255d1c3
main_link = 'https://api.openweathermap.org/data/2.5/weather'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
city = 'Kaliningrad'
appid = 'e5e4cd692a72b0b66ea0a6b80255d1c3'

# response = requests.get(f'{main_link}?q={city}&appid={appid}')
params = {'q':city,
          'appid':appid}
response = requests.get(main_link,params=params)
if response.ok:
    data = json.loads(response.text)
    # pprint(data)
    print(f"В городе {data['name']} температура {data['main']['temp'] - 273.15} градусов")
