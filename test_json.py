#! /usr/bin/python 
# -*- coding: utf-8 -*-

import requests
import json

payload = {"id": 19, "name": "hm"}
headers = {'content-type': 'application/json'}
r = requests.post('http://127.0.0.1:8000/polls/test_json/', data=json.dumps(payload), headers=headers)
print r.text
