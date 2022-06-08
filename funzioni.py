from http import cookies
from importlib.resources import contents
from bs4 import BeautifulSoup
import lxml
import requests
import os
import shutil

cartella = "C:\\Users\\franc\\Scripts\\anime\\file"

def search(name):

    if not os.path.exists(cartella):
        os.mkdir(cartella)
    
    params = (
        ('search', name),
    )

    cookies = {
    '__ddg1': 'xnXqWmNWqFb4XOuU0KJX',
    'cookieconsent_status': 'ok',
    'PHPSESSID': 'nefn0433nabr33le3nilt9pb84',
    'ASCookie': 'b798ab5eadfe343b990a4f2451d4748d',
    }

    headers = {
    'authority': 'www.animesaturn.it',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-gpc': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.animesaturn.it/?d=1',
    'accept-language': 'en-US,en;q=0.9',
    }

    response = requests.get('https://www.animesaturn.it/animelist', params=params , headers=headers , cookies=cookies)


    with open(f'{cartella}/search.html', 'w', encoding="utf-8") as f:
        f.write(response.text)

    with open(f'{cartella}/search.html','r' ,encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content,'html.parser')

    linkall = soup.find_all("a",class_="thumb image-wrapper")

    link = []
    for l in linkall:
        link.append(l["href"])

    link = list(dict.fromkeys(link))

    #shutil.rmtree(cartella)

    return link

def choose(url):
    if not os.path.exists(cartella):
        os.mkdir(cartella)
    
    cookies = {
    '__ddg1': 'xnXqWmNWqFb4XOuU0KJX',
    'cookieconsent_status': 'ok',
    'PHPSESSID': 'nefn0433nabr33le3nilt9pb84',
    'ASCookie': 'b798ab5eadfe343b990a4f2451d4748d',
    }

    response = requests.get(url , cookies=cookies)
    
    with open(f'{cartella}/choose.html', 'w',encoding="utf-8") as f:
            f.write(response.text)
    
    with open(f'{cartella}/choose.html','r',encoding="utf-8") as f:
            content = f.read()
    
    soup = BeautifulSoup(content,'html.parser')
    
    buttonsR = soup.find_all("a", class_='btn btn-dark mb-1 bottone-ep')
    
    buttons = []
    for b in buttonsR:
            buttons.append(b["href"])

    #shutil.rmtree(cartella)

    return buttons

def episode(url):
    if not os.path.exists(cartella):
        os.mkdir(cartella)

    cookies = {
    '__ddg1': 'xnXqWmNWqFb4XOuU0KJX',
    'cookieconsent_status': 'ok',
    'PHPSESSID': 'nefn0433nabr33le3nilt9pb84',
    'ASCookie': 'b798ab5eadfe343b990a4f2451d4748d',
    }

    response = requests.get(url, cookies=cookies)

    with open(f"{cartella}/episode.html","w",encoding="utf-8") as f:
        f.write(response.text)

    with open(f"{cartella}/episode.html","r",encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content,"html.parser")
    div = soup.find("div",class_="card-body")
    episode = div.a['href']

    #shutil.rmtree(cartella)
    
    return episode

def play(url):
    if not os.path.exists(cartella):
        os.mkdir(cartella)

    cookies = {
    '__ddg1': 'xnXqWmNWqFb4XOuU0KJX',
    'cookieconsent_status': 'ok',
    'PHPSESSID': 'nefn0433nabr33le3nilt9pb84',
    'ASCookie': 'b798ab5eadfe343b990a4f2451d4748d',
    }

    response = requests.get(url, cookies=cookies)

    with open(f"{cartella}/ep.html","w" ,encoding="utf-8") as f:
        f.write(response.text)

    with open(f"{cartella}/ep.html","r",encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    video = soup.find_all('video')

    #print(video)

    if len(video) > 0:
        source = video[0].find_all('source')
        s = str(source)
        link = s.split('"')
        link = link[1]
        _ = os.system(f'vlc --fullscreen {link}')
    else:
        div = soup.find("div",class_="embed-responsive-item")
        #print(div)
        s = div.find_all("script")
        s = str(s[1])
        s = s.split('"')
        link  = s[5]
        _ = os.system(f'vlc --fullscreen {link}')
    
    #shutil.rmtree(cartella)

    return None