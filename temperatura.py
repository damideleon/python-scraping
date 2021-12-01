# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
file = "C:/Users/User/Documents/WEBAPP/pronostico.json"
response = requests.get("https://www.meteorologia.gov.py").text
alertHTML = requests.get("https://www.meteorologia.gov.py/avisos/").text
soup = BeautifulSoup(response, 'html.parser').body
alert = BeautifulSoup(alertHTML, 'html.parser').body


try:
	alerta = {
		"vigencia" : "Alerta vigente",
		"titulo" : alert.find("h3").get_text().strip(),
		"descri_corta" : alert.find_all('p')[2].get_text().strip(),
		"fecha" : alert.find_all('p')[0].get_text().strip(),
		"hora" : alert.find_all('p')[1].get_text().strip()
	}	
except:
	alerta = {}


tiempo = {
	"alerta" : alerta,
	"asuncion" :  {
		"name" : soup.find_all('span', {'class':'city'})[1].get_text().strip(),
		"temp" : soup.find_all('span', {'class':'temp-max'})[1].get_text().strip(),
		"descricorta": soup.find_all('div', {'class':'short-description'})[1].get_text().strip(),
		"presion" : soup.find_all('div', {'class':'precip'})[1].contents[3].get_text().strip(),
		"sensacionTermica" : soup.find_all('span', {'class':'high'})[1].get_text().strip(),
		"humedad" : soup.find_all('div', {'class':'humidity'})[1].div.get_text().strip(),
		"viento" : soup.find_all('span', {'class':'speed'})[1].get_text().strip(),
		"dir": soup.find_all('span', {'class':'dir'})[1].get_text().strip(),
		"actualizacion": soup.find_all('div', {'class': "updated"})[1].get_text().strip(),
		"dia" : [
			{
				"hora": soup.find_all("div", {"class": "w-33"})[0].get_text().strip().split("\n")[0],
				"temp" : soup.find_all("div", {"class": "w-33"})[0].get_text().split("\n")[4].strip(),
				"descripcion": soup.find_all("div", {"class": "w-33"})[0].get_text().split("\n")[6],
				"icon" : soup.find_all("i", {"class": "icon"})[8].get("style").split("'")[1]
			},
			{
				"hora": soup.find_all("div", {"class": "w-33"})[1].get_text().strip().split("\n")[0],
				"temp" : soup.find_all("div", {"class": "w-33"})[1].get_text().split("\n")[4].strip(),
				"descripcion": soup.find_all("div", {"class": "w-33"})[1].get_text().split("\n")[6],
				"icon" : soup.find_all("i", {"class": "icon"})[9].get("style").split("'")[1]
			},
			{
				"hora": soup.find_all("div", {"class": "w-33"})[2].get_text().strip().split("\n")[0],
				"temp" : soup.find_all("div", {"class": "w-33"})[2].get_text().split("\n")[4].strip(),
				"descripcion": soup.find_all("div", {"class": "w-33"})[2].get_text().split("\n")[6],
				"icon" : soup.find_all("i", {"class": "icon"})[10].get("style").split("'")[1]
			}
		]
	},
	"pronostico_extendido" : [
		
		{
			"dia" : soup.find_all("div", {"class": "day-2"})[0].contents[3].get_text().replace("\n", " "),
			"max" :  soup.find_all("div", {"class": "day-2"})[0].contents[5].get_text().replace("\n", " "),
			"min" : soup.find_all("div", {"class": "day-2"})[0].contents[7].get_text().replace("\n", " "),
			"description": soup.find_all("div", {"class": "day-2"})[0].contents[9].get_text().replace("\n", " "),
			"icon" : soup.find_all("div", {"class": "day-2"})[0].contents[1].get("style").split("'")[1]
		},
		{
			"dia" : soup.find_all("div", {"class": "day-3"})[0].contents[3].get_text().replace("\n", " "),
			"max" :  soup.find_all("div", {"class": "day-3"})[0].contents[5].get_text().replace("\n", " "),
			"min" : soup.find_all("div", {"class": "day-3"})[0].contents[7].get_text().replace("\n", " "),
			"description": soup.find_all("div", {"class": "day-3"})[0].contents[9].get_text().replace("\n", " "),
			"icon" : soup.find_all("div", {"class": "day-3"})[0].contents[1].get("style").split("'")[1]
		},
		{
			"dia" : soup.find_all("div", {"class": "day-4"})[0].contents[3].get_text().replace("\n", " "),
			"max" :  soup.find_all("div", {"class": "day-4"})[0].contents[5].get_text().replace("\n", " "),
			"min" : soup.find_all("div", {"class": "day-4"})[0].contents[7].get_text().replace("\n", " "),
			"description": soup.find_all("div", {"class": "day-4"})[0].contents[9].get_text().replace("\n", " "),
			"icon" : soup.find_all("div", {"class": "day-4"})[0].contents[1].get("style").split("'")[1]
		},
		{
			"dia" : soup.find_all("div", {"class": "day-5"})[0].contents[3].get_text().replace("\n", " "),
			"max" :  soup.find_all("div", {"class": "day-5"})[0].contents[5].get_text().replace("\n", " "),
			"min" : soup.find_all("div", {"class": "day-5"})[0].contents[7].get_text().replace("\n", " "),
			"description": soup.find_all("div", {"class": "day-5"})[0].contents[9].get_text().replace("\n", " "),
			"icon" : soup.find_all("div", {"class": "day-5"})[0].contents[1].get("style").split("'")[1]
		}
	]
}

## print(json.dumps(tiempo))

with open(file, 'w') as outfile:
	json.dump(tiempo, outfile)