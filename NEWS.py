
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


response=requests.get('https://www.reuters.com/')
doc=BeautifulSoup(response.text, 'html.parser')


# In[3]:


daily=[]
reutersstories=doc.find_all('div', {'class':'story-content'})
print(len(reutersstories))
print(reutersstories)


# In[4]:


list_of_stories = []

for story in reutersstories:
    story_dict = {}
    try:
        headline = story.find(class_='story-title')
        url=story.find('a')['href']
        if headline:
            story_dict['headline'] = headline.text.strip()
        if url:
            story_dict['url'] = url
        list_of_stories.append(story_dict)
    except:
        pass


# In[5]:


df=pd.DataFrame(list_of_stories)


# In[6]:


df=df.dropna()


# In[8]:


import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("'%Y-%m-%d %I %p'")
time_string=right_now.strftime("'%I %p'")


# In[9]:


filename = "reuters" + date_string + ".csv"


# In[10]:


df.to_csv(filename, index=False)


# In[16]:


response = requests.post(
        "https:///messages",
        auth=("api", ""),
        files=[("attachment", open(filename))],
        data={"from": ">",
              "to": [""],
              "subject": "Here is your"+time_string+"briefing",
              "text": "Attached your news!"}) 
response.text

