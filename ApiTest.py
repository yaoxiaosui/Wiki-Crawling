
import unittest
import json
from flask import Flask,request,jsonify
import requests
app = Flask(__name__)

class ApiTest(unittest.TestCase):
    @app.route('/')
    def test_home_page(self):
        with app.test_request_context():
            response = requests.get('http://127.0.0.1:5000/')
            self.assertEqual(response.status_code, 200)
            print(response.text)
            self.assertEqual(response.text, "hello world")
    def test_get_actor(self):
        with app.test_request_context():
            response = requests.get('http://127.0.0.1:5000/actor/Tom')
            #print(response.json()['Actor']['Actor age'])
            self.assertEqual(response.json()['Actor']['Actor name'],"Tom Holland (actor)")
    def test_get_actor(self):
        with app.test_request_context():
            response = requests.get('http://127.0.0.1:5000/film/Impossible')
            self.assertEqual(response.json()['Film']['Film Name'],"The Impossible (2012 film)")

    def test_put_actor(self):
        with app.test_request_context():
            response = requests.get('http://127.0.0.1:5000/actor/George Pollard Jr.')
            self.assertEqual(response.json()['Actor']['Actor age'],"99")
    def test_put_film(self):
        with app.test_request_context():
            response = requests.get('http://127.0.0.1:5000/film/Billy Elliot the Musical Live')
            self.assertEqual(response.json()['Film']['Box office'],"2.2 billion")

    def test_delete_actor(self):
        with app.test_request_context():
            response = requests.get('http://127.0.0.1:5000/actor/Clive Francis')
            self.assertEqual(response.text,"None")

    def test_post_actor(self):
        with app.test_request_context():
            response = requests.get('http://127.0.0.1:5000/actor/Yuan')
            self.assertEqual(response.json()['Actor']['Actor name'], "Yuan Yao")











