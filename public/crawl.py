from random import randrange;
from bs4  import BeautifulSoup;
import requests ;
import json ;
from selenium import webdriver ;
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time;
def verifyAliment(string):
    banned = ["porc","sanglier","vin","chorizo","jambon","cochon"]
    for word in banned:
        if(word in string) :
            return False

    return True;

from selenium.webdriver.common.keys import Keys; # pour appuyer sur entrer dans un champs de saisi 

ressources = [
    {
        'case' : 1 ,
        'site' : "https://www.marmiton.org/recettes/?page=",
        'max_pages' : 450,
    },
    {
        'case' : 2,
        'site' : "https://www.750g.com/categorie_aperitifs.htm?page=",
        'max_pages' : 518,
    },
    {
        'case' : 2,
        'site' : "https://www.750g.com/categorie_entrees.htm?page=",
        'max_pages' : 2000,
    },
    {
        'case' : 2,
        'site' : "https://www.750g.com/categorie_desserts.htm?page=",
        'max_pages' : 2900,
    },
    {
        'case' : 2,
        'site' : "https://www.750g.com/categorie_plats.htm?page=2474",
        'max_pages' : 2474,
    },
    {
        'case' : 2,
        'site' : "https://www.750g.com/categorie_boissons.htm?page=",
        'max_pages' : 154,
    },
    {
        'case' : 2,
        'site' : "https://www.750g.com/categorie_accompagnements.htm?page=",
        'max_pages' : 422,
    },
    {
        'case' : 2,
        'site' : "https://www.750g.com/categorie_gateaux-biscuits.htm?page=",
        'max_pages' : 610,
    },
    {
        'case' : 2,
        'site' : "https://www.750g.com/categorie_patisserie.htm?page=",
        'max_pages' : 102,
    },
    {
        'case' : 2,
        'site' : "https://www.750g.com/categorie_boulangerie-viennoiserie.htm?page=",
        'max_pages' : 49,
    },
    {
        'case' : 2,
        'site' : "https://www.750g.com/categorie_petit-dejeuner.htm?page=",
        'max_pages' : 53,
    },
    {
        'case' : 2,
        'site' : "https://www.750g.com/categorie_confitures.htm?page=",
        'max_pages' : 72,
    },
    {
        'case' : 2,
        'site' : "https://www.750g.com/categorie_salades.htm?page=",
        'max_pages' : 201,
    },
    {
        'case' : 2,
        'site' : "https://www.750g.com/categorie_sauces.htm?page=",
        'max_pages' : 85,
    },
    {
        'case' : 2,
        'site' : "https://www.750g.com/categorie_soupes.htm?page=",
        'max_pages' : 70,
    },
    {
        'case' : 2,
        'site' : "https://www.750g.com/categorie_tartes.htm?page=", #image à éviter contient default
        'max_pages' : 294,
    },
    {
        'case' : 3,
        'site' : "https://www.regal.fr/recettes?page=",
        'max_pages' : 345,
    },
    {
        'case' : 4,
        'site' : "https://larecette.net/les-recettes/page/" ,
        'max_pages' : 128,
    },
    {
        'case' : 5,
        'site' : "https://www.cuisineaz.com/categories/aperitif-cat48640?page=", # image à éviter contient default
        'max_pages' : 20,
    },
    {
        'case' : 5,
        'site' : "https://www.cuisineaz.com/categories/boissons-cat48664?page=",
        'max_pages' : 50,
    },
    {
        'case' : 5,
        'site' : "https://www.cuisineaz.com/categories/desserts-cat48681?page=",
        'max_pages' : 50,
    },
    {
        'case' : 5,
        'site' : "https://www.cuisineaz.com/categories/entrees-cat48785?page=",
        'max_pages' : 50,
    },
    {
        'case' : 5,
        'site' : "https://www.cuisineaz.com/categories/plats-cat48816?page=",
        'max_pages' : 50,
    },
    {
        'case' : 6,
        'site' : "https://www.cookomix.com/wp-content/uploads/alm-cache/0-00-all-preload/page-",
        'max_pages' : 50,
    },
    {
        'case' : 7,
        'site' : "https://www.cuisineactuelle.fr/content/search?search%5Bkeyword%5D=&search%5Bdishtypes%5D%5B%5D=aperitif&search%5Bsort%5D=&search%5Bdirection%5D=&search%5Bpage%5D=1",
    },
    {
        'case' : 7,
        'site' : "https://www.cuisineactuelle.fr/content/search?search%5Bkeyword%5D=&search%5Bdishtypes%5D%5B%5D=entree&search%5Bsort%5D=ASC&search%5Bdirection%5D=&search%5Bpage%5D=1",
    },
    {
        'case' : 7,
        'site' : "https://www.cuisineactuelle.fr/content/search?search%5Bkeyword%5D=&search%5Bdishtypes%5D%5B%5D=plat&search%5Bsort%5D=ASC&search%5Bdirection%5D=&search%5Bpage%5D=1",
    },
    {
        'case' : 7,
        'site' : "https://www.cuisineactuelle.fr/content/search?search%5Bkeyword%5D=&search%5Bdishtypes%5D%5B%5D=dessert&search%5Bsort%5D=ASC&search%5Bdirection%5D=&search%5Bpage%5D=1",
    },
    {
        'case' : 7,
        'site' : "https://www.cuisineactuelle.fr/content/search?search%5Bkeyword%5D=&search%5Bdishtypes%5D%5B%5D=sauce&search%5Bsort%5D=&search%5Bdirection%5D=&search%5Bpage%5D=1",
    },
    {
        'case' : 7 ,
        'site' : "https://www.cuisineactuelle.fr/content/search?search%5Bkeyword%5D=&search%5Bdishtypes%5D%5B%5D=boisson&search%5Bsort%5D=ASC&search%5Bdirection%5D=&search%5Bpage%5D=1"
    }
];

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36')



trouve = False 
while trouve == False :
    #choix = ressources[randrange(0,len(ressources)-1 )]
    choix = ressources[23]

    headers= {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    if  (choix['case'] == 1) :
        site = choix['site']
        page = randrange(1,choix['max_pages'])
        res = requests.get(site+str(page), headers=headers)
        soup = BeautifulSoup(res.text, 'lxml');
        photos_raw = soup.select('div.recipe-card__picture img');
        links = soup.select('a.recipe-card-link');
        if len(photos_raw) > 0 : 
            photos = []
            for p in photos_raw:
                if("blurred" not in p['src'] and verifyAliment(p['src'])):
                    photos.append(p)
                    j= 0;
                    while j < len(links):
                        src = links[j].select('div.recipe-card__picture img')
                        if( src[0]['src'] == p['src'] ):
                            p['link'] = links[j]['href']
                            j = len(links)
                        j=j+1
            if len(photos) > 0 :
                trouve= True
                photo = photos[randrange(0, len(photos)-1 )]

                return_object = {
                    'link' : photo['link'],
                    'src' :photo['src'] ,
                }
    elif(choix['case'] == 2):
        site = choix['site']
        page = randrange(1,choix['max_pages'])
        res = requests.get(site+str(page), headers=headers)
        soup = BeautifulSoup(res.text, 'lxml');
        photos_raw = soup.select('section.c-recipe-row.c-row');
        sections = []
        for section in photos_raw:
            if("default" not in section.select('img')[0]['data-src'] ) and (verifyAliment(section.select('a')[0]['href'])):
                sections.append(section)
        
        if(len(sections) > 0):
            trouve = True
            item = sections[randrange(0,len(sections)-1)]
            return_object = {
                'src' :  item.select('img')[0]['data-src'],
                'link' : "https://www.750g.com"+item.select('a')[0]['href'],
            }
    elif(choix['case'] == 3):
        site = choix['site']
        page = randrange(1,choix['max_pages'])
        res = requests.get(site+str(page), headers=headers)
        soup = BeautifulSoup(res.text, 'lxml');
        items = soup.select('div.views-row ');
        item = items[randrange(0,len(items)-1)]
        return_object = {
            'src' :  item.select('img')[0]['src'],
            'link' : "https://www.regal.fr"+item.select('a')[0]['href'],
        }
        trouve = True
    elif(choix['case'] == 4):
        site = choix['site']
        page = randrange(1,choix['max_pages'])
        res = requests.get(site+str(page), headers=headers)
        soup = BeautifulSoup(res.text, 'lxml');
        items = soup.select('div.page-body figure.entry-featured-media');
        item = items[randrange(0,len(items)-1)]
        return_object = {
            'src' :  item.select('img')[0]['src'],
            'link' : item.select('a')[0]['href'],
        }
        trouve = True
    elif(choix['case'] == 5) :
        driver = webdriver.Chrome(executable_path=r"chromedriver.exe", options=options)
        site = choix['site']
        page = randrange(1,choix['max_pages'])
        driver.get(site+str(page) )
        time.sleep(5)
        k=0
        while k < 10080 :
            driver.execute_script("window.scrollTo(0, "+str(k)+");")
            k=k+50
        k=0
        soup = BeautifulSoup((driver.page_source).encode('utf-8'), 'lxml');
        photos_raw = soup.select('article.tile.recipe img');
        links = soup.select('article.tile.recipe div.tile_thumbnail a');
        if len(photos_raw) > 0 : 
            photos = [] 
            for p in photos_raw: 
                
                if("default" not in p['data-src']):
                    photos.append(p)
                    j= 0;
                    while j < len(links): # on recherche le lien correponsdant à l'image contenue dans p 
                        
                        src = links[j].select('img')
                        if( src[0]['data-src'] == p['data-src'] ):
                            p['link'] = links[j]['href']
                            j = len(links)
                        j=j+1
            if len(photos) > 0 :
                trouve= True
                photo = photos[randrange(0, len(photos)-1 )]

                return_object = {
                    'link' : "https://www.cuisineaz.com"+photo['link'],
                    'src' :photo['src'] ,
                }
    elif(choix['case'] == 6 ) :
        site = choix['site']
        page = randrange(1,choix['max_pages'])
        res = requests.get(site+str(page)+'.html', headers=headers)
        soup = BeautifulSoup(res.text, 'lxml');
        items = soup.select('.recipe-item')
        item = items[randrange(0,len(items)-1)]
        return_object = {
            'src' :  item.select('figure img')[0]['src'],
            'link' : item.select('.container a')[0]['href'],
        }
        trouve = True
    elif(choix['case'] == 7):
        site = choix['site']
        res = requests.get(site, headers=headers,timeout=5)
        soup = BeautifulSoup(res.text, 'lxml');
        items = soup.select('li.item.m-right-xs')
        maxPages = items[len(items)-1].text
        page = randrange(1,int(maxPages))
        min_diff = int(page)
        i = 0
        lien = ''
        while min_diff != 0 :
            j = 0
            while j < len(items) :
                if items[j].text.strip() != '<' and items[j].text.strip() != '>' and abs(int(items[j].text) - int(page)) < min_diff  :
                    min_diff = abs(int(items[j].text) - int(page))
                    lien = items[j].select('a')[0]['href'];
                if min_diff == 0 :
                    break;
                j=j+1
            res= requests.get('https://www.cuisineactuelle.fr'+lien, headers=headers, timeout=5)
            soup = BeautifulSoup(res.text, 'lxml');
            items = soup.select('li.item.m-right-xs')
            time.sleep(1)
            
        divs = soup.select('div.gallery-image')
        index = randrange(0,len(divs)-1)
        lien = divs[index].select('a.title')[0]['href']
        image = divs[index].select('img')[0]['data-src']
        trouve = True
        return_object = {
                    'link' : 'https://www.cuisineactuelle.fr'+lien,
                    'src' :image,
                }
        break
    

if trouve == True :
    print(json.dumps(return_object))
exit()