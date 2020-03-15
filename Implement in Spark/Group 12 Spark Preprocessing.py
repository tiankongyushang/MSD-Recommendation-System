# -*- coding: utf-8 -*-
"""
Created on Sun May  5 18:44:00 2019

@author: MagicDi
"""

import pandas as pd

f = open(r"C:\Users\Jstarry\Desktop\Big data\train_triplets\train_triplets.txt","r")
d = f.read()

dl = d.split('\n')

df = []
for i in range(len(dl)):
    df.append(dl[i].split('\t'))
    
d = pd.DataFrame(df)
u = d[0].unique()
lu = len(u)
s = d[1].unique()
ls = len(s)
lu = [i for i in range(lu)]【
ls = [i for i in range(ls)]
uid = pd.DataFrame(lu,u)
sid = pd.DataFrame(ls,s)
uid.to_csv("uid.csv",index=True,header=False)
sid.to_csv("sid.csv",index=True,header=False)
