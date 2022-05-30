#!/usr/bin/env python
# coding: utf-8

import requests
import pandas as pd
import os

bearer_token = os.environ.get('BEARER_TOKEN')
headers = {"Authorization": "Bearer {}".format(bearer_token)}

url = "https://raw.githubusercontent.com/Expugn/priconne-quest-helper/master/data/character_data.json"
response = requests.request("GET", url, headers=headers).json()

df = pd.DataFrame(response['data'])
df.to_csv('a.csv')
