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


#1. Principle Componect Analysis(PCA): extract features from source code
    #rather than the Abstract syntext tree(AST): Farhan et el. suggest PCA
    #what is reason?
#2. Multinomial logistic regression model(MLR): classify the source code based on pridictions
#3. 2tailed z test: evaluate the proformance of MLR predictors


