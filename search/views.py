from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from bs4 import BeautifulSoup
import requests
import unicodedata
import io
from http import cookies
from .forms import customform


def index(request):
    return render(request, 'index.html')


def result(request):
    link = request.GET['link']
    strn = request.GET['strn']
    newspaper = request.GET['newspaper']
    prothomalo = []
    bdnws24 = []
    Jugantor = []
    pratidin = []
    nayadiganta = []
    x = newspaper.split()
    for x in x:
        if x in "prothomalo":
            source = requests.get('https://www.prothomalo.com/' + link).text
            soup = BeautifulSoup(source, 'lxml')
            for posts in soup.find_all('div',
                                       class_=['content_capability_blog', 'content_type_article ',
                                               'responsive_image_hide_']):
                headline = posts.find('span', class_='title').text.strip()
                if strn in headline:
                    link = "https://www.prothomalo.com/" + posts.find('a', class_='link_overlay')['href']
                    result = {'headline': headline, 'link': link}
                    if result not in prothomalo:
                        prothomalo.append(result)
        if x in "BDnews24":
            if "sports" in link:
                link = "sport"
            if "international" in link:
                link = ""
            source = requests.get('https://bangla.bdnews24.com/' + link).text
            soup = BeautifulSoup(source, 'lxml')
            for posts in soup.find_all('a'):
                headline = posts.text.strip()
                if strn in headline:
                    link = posts['href']
                    result = {'headline': headline, 'link': link}
                    if result not in bdnws24:
                        bdnws24.append(result)

        if x in "Jugantor":
            source = requests.get('https://www.jugantor.com/' + link).text
            soup = BeautifulSoup(source, 'lxml')
            for posts in soup.find_all('a'):
                headline = posts.text.strip()
                if strn in headline:
                    link = posts['href']
                    result = {'headline': headline, 'link': link}
                    if result not in Jugantor:
                        Jugantor.append(result)

        if x in "pratidin":
            source = requests.get('https://www.bd-pratidin.com/' + link).text
            soup = BeautifulSoup(source, 'lxml')
            for posts in soup.find_all('a'):
                headline = posts.text.strip()
                if strn in headline:
                    link = "http://dailynayadiganta.com/" + posts['href']
                    result = {'headline': headline, 'link': link}
                    if result not in pratidin:
                        pratidin.append(result)

        if x in "nayadiganta":
            if "sports" in link:
                link = "sports/11"
            if "international" in link:
                link = "international/8"
            source = requests.get('http://dailynayadiganta.com/' + link).text
            soup = BeautifulSoup(source, 'lxml')
            for posts in soup.find_all('a'):
                headline = posts.text.strip()
                if strn in headline:
                    link = posts['href']
                    result = {'headline': headline, 'link': link}
                    if result not in nayadiganta:
                        nayadiganta.append(result)

    return render(request, 'result.html',
                  {'a': prothomalo, 'b': bdnws24, 'j': Jugantor, 'p': pratidin, 'n': nayadiganta})

def custom(request):
    link = request.GET['link']
    strn = request.GET['strn']
    custom = []
    if link not in " ":
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')
        for posts in soup.find_all('a'):
            headline = posts.text.strip()
            if strn in headline:
                link = posts['href']
                result = {'headline': headline, 'link': link}
                if result not in custom:
                    custom.append(result)
    return render(request, 'custom.html', {'custom': custom, 'name': request.GET["link"]})
