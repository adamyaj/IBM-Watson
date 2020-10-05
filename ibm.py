#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install ibm_watson wget')


# In[2]:


from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# In[3]:


url_s2t = "https://stream.watsonplatform.net/speech-to-text/api"


# In[4]:


iam_apikey_s2t = "55U8PradckiJLME0lkhlVHp8cTH24t5OXT5zhT81sICn"


# In the code below i am creating an object to connect to my api using endpoint url and api key.

# In[5]:


authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t


# In[6]:


import wget
url = 'http://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/PolynomialRegressionandPipelines.mp3'


# In[7]:


filename = wget.download(url, '.mp3')


# In[8]:


with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')


# In[9]:


response.result


# In[10]:


from pandas.io.json import json_normalize

json_normalize(response.result['results'],"alternatives")


# In[11]:


response


# In[12]:


recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)
