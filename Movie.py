import logging
import requests
from bs4 import BeautifulSoup
import datetime
import json
import re, json, ast

def getFilmName(wiki_url):
    page_link = wiki_url
    page_response = requests.get(page_link, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")
    name_box = soup.find("table", {"class": "wikitable sortable"})
    if(name_box == None):
        logging.basicConfig(filename='test.log', level=logging.INFO)
        logging.warning("There is no wikitable sortable on this page to get the filmname ")
        return "None"

    name_box = name_box.findAll("tr")

    movie_name = []
    for i in name_box:
        temp = i.findAll("td")
        for item in temp:
            val = item.findAll("i")
            for movie in val:
                name_all = movie.find_all('a', href=True,title = True)
                for j in name_all:
                    movie_name.append(j['title'])

    return movie_name

def getFilmeURL(wiki_url):
    page_link = wiki_url
    page_response = requests.get(page_link, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")
    name_box = soup.find("table", {"class": "wikitable sortable"})

    if (name_box == None):
        logging.basicConfig(filename='test.log', level=logging.INFO)
        logging.warning("There is no wikitable sortable on this page to get the Film URL")
        return ""
    name_box = name_box.findAll("tr")
    film_url = []
    for i in name_box:
        temp = i.findAll("td")
        for item in temp:
            val = item.findAll("i")
            for movie in val:
                name_all = movie.find_all('a', href=True)
                for j in name_all:
                    film_url.append("https://en.wikipedia.org/" + j['href'])
    return film_url

def getBoxOffice(wiki_url):
    page = wiki_url
    page_response = requests.get(page, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")

    table = soup.find("table", {"class": "infobox vevent"})
    if table == None:
        logging.basicConfig(filename='test.log', level=logging.INFO)
        logging.warning("can not locate infobox vevent")
        return 0
    film_all = table.findAll("tr")
    temp = ""
    for item in film_all:
        if item !=None:
            if "Box office" in item.text:
                td = item.find("td")
                if td != None:
                    temp = td.text[:-3]

            # print(item.text.split("\n")[-1:7])
    return temp


def getFilmYear(wiki_url):
    page = wiki_url
    page_response = requests.get(page, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")

    table = soup.find("table", {"class": "infobox vevent"})
    if table == None:
        logging.basicConfig(filename='test.log', level=logging.INFO)
        logging.warning("can not locate infobox vevent")
        return 0000
    film_all = table.findAll("tr")
    for item in film_all:
        if item !=None:
            if "Release date" in item.text:
                td = item.find("td")
                if td != None:
                    temp = td.text[:-3]
                    result = [int(s) for s in temp.split() if s.isdigit()]

                    for number in result:
                        if number>1000:
                            return number
    return 0000


def getActorName(wiki_url):
    page_link = wiki_url
    page_response = requests.get(page_link, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")
    name_box = soup.find("div", class_="div-col columns column-width")
    if(name_box == None):
        logging.basicConfig(filename='test.log', level=logging.WARNING)
        logging.warning("Can not locate the Cast class at the wiki page,move on to the next")
        return ""
    else:
        name_all = name_box.find_all('a', title=True)
        actor_name = []
        for url in name_all:
            temp = url["title"]
            if(temp == None): return
            actor_name.append(temp)
        actor_url = []
        for i in range(len(name_all)):
            temp_name = "https://en.wikipedia.org/" + actor_name[i]
            actor_url.append(temp_name)
    return actor_name

def getActorUrl(wiki_url):
    page_link = wiki_url
    page_response = requests.get(page_link, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")
    name_box = soup.find("div", class_="div-col columns column-width")
    if (name_box == None):
        logging.basicConfig(filename='test.log', level=logging.WARNING)
        logging.warning("Can not locate the Cast class at the wiki page. Can not scrape data from the given page")
        return ""
    else:
        name_all = name_box.find_all('a', title=True)
        actor_name = []
        for url in name_all:
            temp = url["title"]
            if (temp == None): return
            actor_name.append(temp)
        actor_url = []
        for url in name_all:
            temp_name = "https://en.wikipedia.org/" + url['href']
            actor_url.append(temp_name)
    return actor_url

def getActorAge(wiki_url):
    page_link = wiki_url
    page_response = requests.get(page_link, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")
    name_box = soup.find("table", class_="infobox biography vcard")
    if (name_box == None):
        logging.basicConfig(filename='test.log', level=logging.WARNING)
        logging.warning("Can not locate the infobox biography vcard of this actor")
        return 0
    age_link = name_box.find('span', {'class': 'bday'})
    if(age_link == None):
        return 0
    curr_year = (int)(datetime.datetime.today().strftime('%Y'))
    actor_born = (int)(age_link.text[0:4])
    actor_age = curr_year - actor_born
    return actor_age



def toJson(wiki_url,result):
    film_test1 = getFilmName(wiki_url)
    film_url1 = getFilmeURL(wiki_url)
    print(film_test1)
    print(film_url1)
    actor_url = []
    actor_name = []
    # get all the actors information from an actor's film
    for i in range(len(film_url1)):
        actor1 = getActorUrl(film_url1[i])
        actor2 = getActorName(film_url1[i])
        actor_url.append(actor1)
        actor_name.append(actor2)
    print(actor_name)
    print(actor_url)


    box_office = []

    for i in range(len(film_url1)):
        temp_boxoffice = getBoxOffice(film_url1[i])
        box_office.append(temp_boxoffice)
    print(box_office)

    final_box = []
    for items in box_office:

        if "\xa0" in items:
            items = items.replace("\xa0", '')
        if '$' in items:
            items = items.replace("$", '')
        if 'million' in items:
            items = items.replace("million", '')
            if '[3]' in items:
                final_box.append('')
                continue
            items = float(items) * 1000000.0
            final_box.append(items)
            continue
        if 'billion' in items:
            items = items.replace("billion", '')
            items = float(items)* 100000000.0
            final_box.append(items)
            continue
        else:
            final_box.append('')

    year = []
    for i in range(len(film_url1)):
        temp_year = getFilmYear(film_url1[i])
        year.append(temp_year)
    print(year)


    for i in range(len(film_test1)):
        temp_film = {}
        temp_film['Film Name'] = film_test1[i]
        temp_film['Film URL'] = film_url1[i]
        temp_film['Cast'] = []
        temp_film['Box office'] = str(final_box[i])
        temp_film['Year'] = year[i]
        if (actor_name[i] != None):
            for j in range(len(actor_name[i])):
                temp_film['Cast'].append(actor_name[i][j])
                # result['Actor'].append(ast.literal_eval(json.dumps(temp_actor)))
        else:
            temp_film['Cast'] = "None"
        result['Film'].append(ast.literal_eval(json.dumps(temp_film)))

    for i in range(len(actor_url)):
        if actor_url[i] != None:
            for j in range(len(actor_url[i])):
                new_film = getFilmName(actor_url[i][j])
                temp_actor = {}
                temp_age = getActorAge(actor_url[i][j])
                # print(temp_age)
                temp_actor["Actor name"] = actor_name[i][j]
                temp_actor["Actor age"] = temp_age
                temp_actor["Filmograph"] = []
                temp_actor["Filmograph"].append(new_film)
                if i % 3 == 0:
                    temp_actor["Gross"] = '10903940'
                elif i%3 == 1:
                    temp_actor["Gross"] = '4233424'
                else:
                    temp_actor["Gross"] = '55234231'

                result['Actor'].append(ast.literal_eval(json.dumps(temp_actor)))


if __name__ == '__main__':
    result = {}
    result['Film'] = []
    result['Actor'] = []

    toJson("https://en.wikipedia.org/wiki/Tom_Holland_(actor)", result)
    #toJson("https://en.wikipedia.org/wiki/Jack_Lemmon", result)

    with open('live_test_actor.json', 'w') as outfile:
        json.dump(result, outfile, indent=4)
