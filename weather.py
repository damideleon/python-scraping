##api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}&lang=es
import requests
r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=asuncion&appid=[apiKEY]&lang=es").json()
t = r['main']['temp'] 
print(round(t-273.15))
