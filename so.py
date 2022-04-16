import requests
from bs4 import BeautifulSoup

URL = f'https://stackoverflow.com/jobs/companies?q=python'

def get_last_page():
    result = requests.get(URL) 
    soup = BeautifulSoup(result.text, 'html.parser')
    pages = soup.find('div', {'class': 's-pagination'}).find_all('a')
    lst = []

    for page in pages[:-1]:
        lst.append(int(page.find('span').string))

    max_page = lst[-1]
    return max_page
    

def get_jobs():
    last_page = get_last_page()
    return last_page