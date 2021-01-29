import requests 
import pandas as pd
import re

# match UCL email address by and .xlsx filr

f = open('group_export.txt', "r")
t = f.read()

emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", t)
print (emails)

f.close

r = requests.get('https://api.github.com/users/zczllw5')
print(r.text)

#''['[]]