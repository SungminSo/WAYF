
# coding: utf-8

# In[1]:


# -*- coding:utf-8 -*-
import requests
import shutil
import os
from collections import defaultdict


# In[2]:


ID_URL = defaultdict(list)

with open("./valid_data.csv", "r", encoding="UTF-8") as f:
    for i in map(lambda x: x.split(','), f):
        ID_URL[i[3].strip()].append((i[0], i[2]))

del ID_URL["Nationality"]


# In[3]:


"""

cnt = 0
for nation, temp in ID_URL.items():
    for ID, URL in temp:
        r = requests.get(URL, stream=True)
        if r.status_code == 200:
            cnt += 1
            
            path = f"./valid_pictures/{nation}"
            if not os.path.isdir(path):
                os.mkdir(path)
            
            with open(f"{path}/{ID}.png", "wb") as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
            
            print(cnt, ID, URL)
"""


# In[4]:


list(ID_URL.keys())[14:]


# In[ ]:


cnt = 0

for nation, temp in list(ID_URL.items())[14:]:
    for ID, URL in temp:
        try:
            r = requests.get(URL, stream=True)
            if r.status_code == 200:
                path = f"./valid_pictures/{nation}"

                try:
                    with open(f"{path}/{ID}.png", "r") as f:
                        print(cnt, "Already Downloaded")

                except:
                    if not os.path.isdir(path):
                        os.mkdir(path)

                    with open(f"{path}/{ID}.png", "wb") as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
                        cnt += 1

                    print(cnt, ID, URL)
            else:
                print(cnt, "Download Failed")
        except:
            print("FATAL ERROR", ID, URL)
            pass
