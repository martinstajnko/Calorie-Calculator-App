import requests
from bs4 import BeautifulSoup


class Temperature:

    """

    """

    base_url = 'https://www.timeanddate.com/weather/'


    def __init__(self, country, city):
        self.country = country.replace(' ', '-')
        self.city = city.replace(' ', '-')


    def build_url(self):
        url = self.base_url + self.country + "/" + self.city
        return url


    def scrape_for_temperature(self):
        url = self.build_url()
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        print('*' * 10)
        results = soup.find(id='qlook')
        return results


    def get_temperature(self):
        results = self.scrape_for_temperature()
        if results == None:
            return 'Error' 
        #
        get_temperatur = results.find("div", class_="h2")
        temperature = get_temperatur.getText()
        # We want to get only number
        temperature = temperature.replace('\xa0°C', '')
        return float(temperature)
        


print(__name__)
if  __name__ == "__main__":
    temperature = Temperature(country='slovenia', city='murska sobota')
    print(temperature.get_temperature())
