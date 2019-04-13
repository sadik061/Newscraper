from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from bs4 import BeautifulSoup
import requests
import unicodedata
import io
from http import cookies


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
    C = cookies.SimpleCookie()
    print(C)
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
                    if result not in pratidin:
                        prothomalo.append(result)
        if x in "BDnews24":
            source = requests.get('https://bangla.bdnews24.com/').text
            soup = BeautifulSoup(source, 'lxml')
            for posts in soup.find_all('a'):
                headline = posts.text.strip()
                if strn in headline:
                    link = posts['href']
                    result = {'headline': headline, 'link': link}
                    if result not in pratidin:
                        bdnws24.append(result)

        if x in "Jugantor":
            source = requests.get('https://www.jugantor.com/').text
            soup = BeautifulSoup(source, 'lxml')
            for posts in soup.find_all('a'):
                headline = posts.text.strip()
                if strn in headline:
                    link = posts['href']
                    result = {'headline': headline, 'link': link}
                    if result not in pratidin:
                        Jugantor.append(result)

        if x in "pratidin":
            source = requests.get('https://www.bd-pratidin.com/').text
            soup = BeautifulSoup(source, 'lxml')
            for posts in soup.find_all('a'):
                headline = posts.text.strip()
                if strn in headline:
                    link = "http://dailynayadiganta.com/"+posts['href']
                    result = {'headline': headline, 'link': link}
                    if result not in pratidin:
                        pratidin.append(result)
                        print(pratidin)

        if x in "nayadiganta":
            source = requests.get('http://dailynayadiganta.com/').text
            soup = BeautifulSoup(source, 'lxml')
            for posts in soup.find_all('a'):
                headline = posts.text.strip()
                if strn in headline:
                    link = posts['href']
                    result = {'headline': headline, 'link': link}
                    if result not in pratidin:
                        nayadiganta.append(result)

    return render(request, 'result.html', {'a': prothomalo, 'b': bdnws24, 'j': Jugantor, 'p': pratidin, 'n': nayadiganta})
