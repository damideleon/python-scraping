import requests
import json
from bs4 import BeautifulSoup

def descargarTabla(url, file, titulo, torneo):
	tabla = []
	page = requests.get(url).text
	soup = BeautifulSoup(page, 'html.parser')
	table = soup.find('table', id="pos_n1")
	row = table.find_all('tr', class_= "linea")
	for data in row:
		r = {
			"pos": data.find_all("td")[0].get_text(),
			"equipo": data.find_all("td")[2].get_text(),
			"puntos": data.find_all("td")[3].get_text(),
			"pj": data.find_all("td")[4].get_text(),
			"pg": data.find_all("td")[5].get_text(),
			"pe": data.find_all("td")[6].get_text(),
			"pp": data.find_all("td")[7].get_text(),
			"gf": data.find_all("td")[8].get_text(),
			"gc": data.find_all("td")[9].get_text(),
			"dif": data.find_all("td")[10].get_text()
		}
		tabla.append(r)
	with open(file, 'w') as outfile:
		json.dump({
			"tabla": tabla,
			"torneo": torneo,
			"titulo":titulo
		}, outfile)

## Tabla Posiciones APF Futbol de Primera
descargarTabla("https://estaticopy.tigocloud.net/datafactory/html/v3/htmlCenter/data/deportes/futbol/paraguay/pages/es/posiciones.html",
'C:/Users/User/Documents/WEBAPP/deportes/tabla_de_posiciones_paraguay.json', "Fútbol de primera", "Clausura 2021")
##Tabla de posiciones Intermedia
##descargarTabla("")
##Tabla de p Eliminatorias
descargarTabla("https://estaticopy.tigocloud.net/datafactory/html/v3/htmlCenter/data/deportes/futbol/eliminatorias/pages/es/posiciones.html",
'C:/Users/User/Documents/WEBAPP/deportes/tabla_de_posiciones_eliminatorias.json', "Clasificatorias | CONMEBOL", "Mundial Qatar 2022")
