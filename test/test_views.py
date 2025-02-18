import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in rv.data

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        self.assertEquals('{ "imie":"Bartosz", "mgs":"Hello World!"}', rv.data)

    def test_msg_with_output(self):
        rv = self.app.get('/?output=xml')
        self.assertEquals('<greetings><name>Bartosz</name><msg>Hello World!</msg></greetings>', rv.data)

    def test_msg_with_output_name(self):
        imie = "Wojtek"
        rv = self.app.get('name=' + imie + '&output=json')
        self.assertEquals('{"imie":' + imie + ', "msg": "Hello World!"}', rv.data)
