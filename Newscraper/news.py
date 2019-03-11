from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.prothomalo.com/bangladesh/article').text

soup = BeautifulSoup(source, 'lxml')

for posts in soup.find_all('div', class_='info has_ai'):
    headline = posts.find('span', class_='title').text
    print(headline)