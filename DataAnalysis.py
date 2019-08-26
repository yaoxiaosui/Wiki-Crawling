import numpy
import matplotlib.pyplot as plt
import json
from itertools import groupby
from operator import itemgetter
import operator


def getAgeGross(data):
    actor = data['Actor']
    temp = []
    for items in actor:
        if int(items['Actor age']) > 0:
            temp.append((int(items['Actor age']),int(items['Gross'])))

    result = sorted(temp, key=lambda x: x[0])
    result = [(k, list(list(zip(*g))[1])) for k, g in groupby(result, itemgetter(0))]
    #this code was taken from the stack overflow.
    #https://stackoverflow.com/questions/45476509/group-list-of-tuples-efficiently/45476671
    gross_result = []
    for items in result:
        count = 0
        for key2 in items[1]:
            count += key2
        gross_result.append((items[0], count))
    # print(gross_result)
    x_axis = []
    y_axis = []
    for i in range(len(gross_result)):
        x_axis.append(gross_result[i][0])
        y_axis.append(gross_result[i][1])
    # this code (line 37-39) was taken from the stack overflow.
    # https://stackoverflow.com/questions/17478779/make-scatter-plot-from-set-of-points-in-tuples/17478866
    plt.plot(x_axis, y_axis)
    plt.show()

    return gross_result


def findHub(data):
    actor = data['Actor']
    actor_name = []
    film = data['Film']

    for items in actor:
        actor_name.append(items['Actor name'])
    hub = []
    for items in film:
        if len(items['Cast'])!= 0:
            count = 0
            for cast in items['Cast']:
                for i in range(len(actor_name)):
                    if actor_name[i] == cast:
                        count = count + len(items['Cast'])
                        hub.append((actor_name[i],count))
    x_axis = []
    y_axis = []
    for i in range(len(hub)):
        x_axis.append(hub[i][0])
        y_axis.append(hub[i][1])
    plt.bar(x_axis,y_axis)
    plt.show()
    temp = []
    for i in range (len(hub)):
        temp.append(hub[i][1])
    index, value = max(enumerate(temp), key=operator.itemgetter(1))# this code is take from: https://stackoverflow.com/questions/6193498/pythonic-way-to-find-maximum-value-and-its-index-in-a-list
    print(hub[index][0])
    return hub[index]

if __name__ == '__main__':
    data =  open('data_test.json').read()
    data = json.loads(data)
    test1 = getAgeGross(data)
    test2 = findHub(data)



