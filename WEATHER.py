
# coding: utf-8

# In[73]:


response=requests.get('https://api.darksky.net/forecast/fb771229e4004e19f28d3e05c2053b6b/40.7128,-74.0060?units=si')


# In[75]:


data = response.json()


# In[76]:


#print('Right now it is', data['currently']['temperature'], 'degrees out and', data['currently']['summary'],'. Today will be', data['currently']['apparentTemperature'], 'with a high of', data['daily']['data'][0]['temperatureHigh'], 'and a low of', data['daily']['data'][0]['temperatureLow'],'.There is a',data['daily']['data'][0]['precipProbability'] ,'probability of precipitation.')


# In[77]:


text='Right now it is', data['currently']['temperature'], 'degrees out and', data['currently']['summary'],'. Today will be', data['currently']['apparentTemperature'], 'with a high of', data['daily']['data'][0]['temperatureHigh'], 'and a low of', data['daily']['data'][0]['temperatureLow'],'.There is a',data['daily']['data'][0]['precipProbability'] ,'probability of precipitation.'


# In[81]:


import requests
response = requests.post(
        "https:///messages",
        auth=("api", ""),
        data={"from": ">",
              "to": [""],
              "subject": "Hello",
              "text": text}) 
response.text



