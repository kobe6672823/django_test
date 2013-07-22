#! /usr/bin/python 
# -*- coding: utf-8 -*-

import requests

r = requests.post('http://127.0.0.1:8000/polls/test_req/')
print r.text

sessionid = r.cookies['sessionid']
cookies = {'sessionid': sessionid}
r = requests.get('http://127.0.0.1:8000/polls/test_req/', cookies = cookies)
print r.text
