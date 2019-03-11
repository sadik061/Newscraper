from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from bs4 import BeautifulSoup
import requests
import unicodedata
import io


def index(request):
    return render(request, 'index.html')


def result(request):
    link = request.GET['link']
    strn = request.GET['strn']
    newspaper = request.GET['newspaper']
    prothomalo = []
    bdnws24 = []
    x = newspaper.split()
    for x in x:
        if x in "prothomalo":
            source = requests.get('https://www.prothomalo.com/' + link).text
            soup = BeautifulSoup(source, 'lxml')
            for posts in soup.find_all('div',
                                       class_=['content_capability_blog', 'content_type_article ',
                                               'responsive_image_hide_']):
                headline = posts.find('span', class_='title').text
                if strn in headline:
                    link = "https://www.prothomalo.com/" + posts.find('a', class_='link_overlay')['href']
                    result = {'headline': headline, 'link': link}
                    prothomalo.append(result)
        if x in "BDnews24":
            source = requests.get('https://bangla.bdnews24.com/').text
            soup = BeautifulSoup(source, 'lxml')
            for posts in soup.find_all('a'):
                headline = posts.text
                if strn in headline:
                    link = posts['href']
                    result = {'headline': headline, 'link': link}
                    print(headline)
                    bdnws24.append(result)
    return render(request, 'result.html', {'a': prothomalo, 'b': bdnws24})
