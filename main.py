import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "https://www.marca.com/resultados/futbol/milan/estadisticas/C120.html#120_0107"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
tag = soup.find_all('tr')[1]
tds = tag.find_all('td')

elementos = []

for td in tds:
    elementos.append(float(td.get_text()))

print(elementos)