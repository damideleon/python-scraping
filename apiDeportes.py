import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://es.wikipedia.org/wiki/Torneo_Clausura_2021_(Paraguay)').text
soup = BeautifulSoup(page, 'html.parser')
table = soup.find_all('table')[9]

df = pd.read_html(str(table))
df = pd.concat(df)
print(df)
df.to_csv("elections.csv", index=False)