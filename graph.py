import logging
import requests
from bs4 import BeautifulSoup
import datetime
import json
import re, json, ast
import operator


def getOldestActor(actor):
    age = []
    for items in actor:
        temp_age = items['Actor age']
        age.append(temp_age)
    index, value = max(enumerate(age), key=operator.itemgetter(1)) # this code is taken from: https://stackoverflow.com/questions/6193498/pythonic-way-to-find-maximum-value-and-its-index-in-a-list
    oldestActorName = actor[index]['Actor name']
    print('The oldest actor is',oldestActorName, 'and his age is',value,)
    return value

def getMovieCasting(film):
    temp = []
    for items in film:
        name = items['Film Name']
        temp.append(name)
    print(temp)
    cast = []
    film_name = input("Which casting would you like to see from a certain movie? \n")
    for items in film:
        temp_name = items['Film Name']
        if film_name == temp_name:
            cast = items['Cast']
            print("Here is the cast information for the movie: \n ",cast,)
    if(len(cast)==0): print("please enter a valid Film name")
    return cast

def getActorFilm(actor):
    temp = []
    for items in actor:
        name = items['Actor name']
        temp.append(name)
    print(temp)
    film_name = []
    actor_name = input("Which actor's filmography would you like to see ? \n")
    for items in actor:
        temp_name = items['Actor name']
        if actor_name == temp_name:
            film_name = items['Filmograph']
            print("Here is the filmography for the actor: \n ", film_name, )
    if (len(film_name) == 0): print("please enter a valid Actor name")
    return film_name

def getFilmBoxOffice(film):
    temp = []
    for items in film:
        name = items['Film Name']
        temp.append(name)
    print(temp)
    box_office = []
    film_name = input("Which film's box office would you like to see ? \n")
    for items in film:
        temp_name = items['Film Name']
        if film_name == temp_name:
            box_office = items['Box office']
            print("Here is the box office for the film:", box_office, )
    if (len(box_office) == 0): print("please enter a valid film name")
    return box_office

def getActorAge(actor):
    age = input("Please enter an actor age\n")
    if(int(age) < 0):
        print("Please enter a valid age\n")
        return
    actor_list = []
    for items in actor:
        temp_age = items['Actor age']
        if int(temp_age) == int(age):
            actor_list.append(items['Actor name'])
    if(len(actor_list)==0):
        print("There is no age information for what you entered\n")
        return
    else:
        print("Here is the actors that have the same age",actor_list,)
        return actor_list


def getFilmYear(film):
    year = input("Please enter an film year\n")
    if (int(year) < 0):
        print("Please enter a valid year\n")
        return
    film_list = []
    for items in film:
        temp_year = items['Year']
        if int(temp_year) == int(year):
            film_list.append(items['Film Name'])
    if (len(film_list) == 0):
        print("There is no age information for what you entered\n")
        return
    else:
        print("Here is the films that are realesed in the same year", film_list, )
        return film_list


if __name__ == "__main__":
    with open('live_test_actor.json') as f:
        data = json.load(f)
    film = data["Film"]
    actor = data["Actor"]
