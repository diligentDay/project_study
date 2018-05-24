#coding:utf-8
import unittest
from test4_login import app
import json
class LoginTestCase(unittest.TestCase):
    def setUp(self):
        seflf.client = app.test_client()
    def test_empty_username_password(self):
        client = app.test_client()
        response = client.post('/login',data={'username':'aaaa'})
        response_data = response.data
        response_json = json.loads(response_data)
        
        self.assertIn('errcode',response_json,'None errcode')
        errcode = response_json['errcode']
        self.assertEqual(errcode,-2,'errcode current is %s') % errcode
    def test_error_username_password(self):
        client = app.test_client()
        response = client.post('/login',data={'username':'aaaaa','password':'bbb'})
        response_data = response.data
        response_json = json.loads(response_data)
    
        self.assertIn('errcode',response_json,'None errcode')
        errcode = response_json['errcode']
        self.assertEqual(errcode, -1,'errcode current is %s' % errcode)
if __name__ == '__main__':
    unittest.main()
       
        


        

