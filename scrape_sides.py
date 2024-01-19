import requests
from bs4 import BeautifulSoup
import json

def scrape(URL):
    #automatically scrape nyt for the letters
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    scripts = soup.find_all('script')[2].text[18:] #this is so scuffed but I literally can't be bothered
    test = json.loads(scripts)

    return test['sides']


if __name__ == '__main__':
    URL = 'https://www.nytimes.com/puzzles/letter-boxed'
    print(scrape(URL))