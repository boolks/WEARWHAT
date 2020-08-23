import urllib.request
import json

city = 'Seoul'

url_data = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Seoul&APPID=e779cdc25e091119d383af1b5fd5ea6e")

weather_data = url_data.read()
j = json.loads(weather_data)

weather = j['weather'][0]["main"]
temperature = int(j['main']['temp'] - 273.15)
print('서울의 현재날씨', weather, "온도: ", temperature)