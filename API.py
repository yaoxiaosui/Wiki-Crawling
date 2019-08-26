from flask import Flask,request,jsonify
import json
app = Flask(__name__)


@app.route('/')
def index():
    return "hello world"

@app.route('/actor/<name>')
def getFirstActorName(name):
    actor = data['Actor']
    for items in actor:
        temp_name = str(items['Actor name'])
        if str(name) in temp_name:
            return jsonify({'Actor': items})
    return "None"


@app.route('/actor')
def getAllActorName():
    name = request.args.get('Actor name')
    actor = data['Actor']
    result = {}
    temp = []
    for items in actor:
        temp_name = str(items['Actor name'])
        if str(name) in temp_name:
            temp.append(items)
    if len(temp) == 0: return 'None'
    else:
        result['Actor'] = temp
        return  jsonify(result)


@app.route('/film/<name>')
def getFirstFilmName(name):
    actor = data['Film']
    for items in actor:
        temp_name = str(items['Film Name'])
        if str(name) in temp_name:
            return jsonify({'Film': items})
    return "None"

@app.route('/film')
def getAllFilmName():
    name = request.args.get('Film Name')
    result = {}
    temp = []
    actor = data['Film']
    for items in actor:
        temp_name = str(items['Film Name'])
        if str(name) in temp_name:
            temp.append(temp_name)
    if len(temp) == 0:
        return 'None'
    else:
        result['Film'] = temp
        return jsonify(result)

@app.route('/actor')
def getMultiActor():
    arg1 = request.args.get('Actor name')
    arg2 = request.args.get('Actor age')
    
    result = []
    for items in data['Actor']:
        if str(arg1) == str(items['Actor name']):
            if str(arg2) == str(items['Actor age']):
                result.append(items)
                return jsonify(result)
    
    return arg1 + "" + arg2

"""
@app.route('/actor/<name>',methods=['PUT'])
def putActorAge(name):
    actor = data['Actor']
    for items in actor:
        temp_name = items['Actor name']
        if name == temp_name:
            items['Actor age'] = request.form.get('Actor age')
            with open('data_test.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
            return items['Actor age']
    return 'None'
"""



@app.route('/actor/<name>',methods=['PUT'])
def putActorGross(name):
    actor = data['Actor']
    for items in actor:
        temp_name = items['Actor name']
        if name == temp_name:
            items['Gross'] = request.form.get('Gross')
            with open('data_test.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
            return items['Gross']
    return 'None'

@app.route('/film/<name>',methods=['PUT'])
def putBoxOffice(name):
    film = data['Film']
    for items in film:
        temp_name = items['Film Name']
        if name == temp_name:
            items['Box office'] = request.form.get('Box office')
            with open('data_test.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
            return items['Box office']
    return 'None'


@app.route('/actor/<name>',methods=['DELETE'])
def deleteActor(name):
    actor = data['Actor']
    for items in actor:
        temp_name = items['Actor name']
        if name == temp_name:
            actor.remove(items)
            with open('data_test.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
            return "Delete Actor Sucessful"
    return 'None'

@app.route('/film/<name>',methods=['DELETE'])
def deleteFilm(name):
    film = data['Film']
    for items in film:
        temp_name = items['Film Name']
        if name == temp_name:
            film.remove(items)
            with open('data_test.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
            return "Delete Film Successful"
    return 'None'


@app.route('/actor',methods=['POST'])
def postActor():
    new_actor = {'Actor name': request.form.get('Actor name'),
                 'Actor age': request.form.get('Actor age'),
                   'Filmograph': request.form.get('Filmograph'),
                   'Gross': request.form.get('Gross')}

    data['Actor'].append(new_actor)
    with open('data_test.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
    return jsonify(data['Actor'])


@app.route('/film',methods=['POST'])
def postFilm():
    new_film = {"Film Name": request.form.get('Film Name'),
            "Film URL": request.form.get('Film URL'),
            "Cast": request.form.get('Cast'),
            "Box office": request.form.get('Box office'),
            "Year": request.form.get('Year')}
    data['Film'].append(new_film)
    with open('data_test.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
    return jsonify(data['Film'])


if __name__ == '__main__':
    data =  open('data_test.json').read()
    data = json.loads(data)
    app.run(debug = True)
