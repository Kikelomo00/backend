from . import user
from app import Flask, jsonify, request

languages = [{'name': 'Javascript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]


@user.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works'})


@user.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages' : languages})

@user.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language' : langs[0]})

@user.route('/lang', methods=['POST'])
def addOne():    
    language = {'name' : request.json['name']}
    
    languages.append(language)
    return jsonify({'languages' : languages})

@user.route('/lang/<string:name>', methods=['PUT'])    
def editOne(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify[{'language' : langs[0]}]


@user.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
    lang = [language for language in languages if language['name'] == name]
    languages.remove(lang[0])
    return jsonify({'languages' : languages})
    