import requests
import json
from bs4 import BeautifulSoup

tabla = []
file = "C:/Users/User/Documents/WEBAPP/deportes/tabla_de_promedios_paraguay.json"
page = requests.get('https://estaticopy.tigocloud.net/datafactory/html/v3/htmlCenter/data/deportes/futbol/paraguay/pages/es/descenso.html').text
soup = BeautifulSoup(page, 'html.parser')
table = soup.find_all('table', class_="table")[0]
row = table.find_all('tr', class_= "linea")

for data in row:
	r = {
		"pos": data.find_all("td")[0].get_text(),
		"equipo": data.find_all("td")[2].get_text(),
		"2019": data.find_all("td")[3].get_text(),
		"2020": data.find_all("td")[4].get_text(),
		"2021": data.find_all("td")[5].get_text(),
		"total": data.find_all("td")[6].get_text(),
		"pj": data.find_all("td")[7].get_text(),
		"prom": data.find_all("td")[8].get_text()
	}
	tabla.append(r)
with open(file, 'w') as outfile:
		json.dump({"tabla": tabla}, outfile)
		