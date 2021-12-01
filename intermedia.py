import requests
import json
from bs4 import BeautifulSoup

tabla = []
file = "C:/Users/User/Documents/WEBAPP/deportes/tabla_acumulativo.json"
page = requests.get('https://es.wikipedia.org/wiki/Torneo_Clausura_2021_(Paraguay)').text
soup = BeautifulSoup(page, 'html.parser')
table = soup.find_all('table')[32].tbody
row = table.find_all("tr")

for data in row:
	r = {
		"pos" : data.contents[1].get_text().strip(),
		"equipo": data.contents[3].get_text().strip(),
		"pts": data.contents[5].get_text().strip(),
		"pj": data.contents[7].get_text().strip(),
		"g": data.contents[9].get_text().strip(),
		"e": data.contents[11].get_text().strip(),
		"p": data.contents[13].get_text().strip(),
		"gf": data.contents[15].get_text().strip(),
		"gc": data.contents[17].get_text().strip(),
		"dif": data.contents[19].get_text().strip()
	}
	tabla.append(r)
tabla.pop(0)
# print(json.dumps(tabla))

with open(file, 'w') as outfile:
	json.dump({"tabla": tabla}, outfile)
		