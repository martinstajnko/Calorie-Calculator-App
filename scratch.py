import requests
from bs4 import BeautifulSoup


URL = "https://www.timeanddate.com/weather/spain/salou"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
#print(soup)
print('*' * 10) 
#print(page)

#results = soup.find(id="bct")
# print(results.prettify())

results = soup.find(id="qlook")

temperatur = results.find("div", class_="h2")
text_temp = temperatur.getText()

others = results.find_all("p")
#others_text = others.getText()

#print(results.prettify())
print(temperatur)
print(text_temp)
#print(others)