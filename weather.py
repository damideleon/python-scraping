##api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}&lang=es
import requests
r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=asuncion&appid=36234f369816fa7c206cf3af2b2c38bc&lang=es").json()
t = r['main']['temp'] 
print(round(t-273.15))