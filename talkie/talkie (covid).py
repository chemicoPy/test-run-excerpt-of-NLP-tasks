import numpy as np
from numpy import *
import pandas as pd
from pandas import DataFrame, Series
from numpy.random import randn
import random
import string
import scipy
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')


welcome_message =  print("I'm COVID-talkie, you chat with me on anything on COVID-19")

dataset = open('COVID-Dialogue-Dataset-English.txt','r')

Description = [] 
Patient = []
Doctor =  [] 



with dataset as p:
    lines = p.readlines()
    
with open('COVID-Dialogue-Dataset-English.txt','w') as p:
    for line in lines:
        if not line.strip("\n").startswith('Dialogue'):
            if not line.strip("\n").startswith('https'):
                if not line.strip("\n").startswith('id='):
                    p.write(line)

            
with open('COVID-Dialogue-Dataset-English.txt', "r") as z:
    for line in lines:
        for line in z:
            if 'Patient' in line:
                Patient.append(next(z))
                
                break
  
    
with open('COVID-Dialogue-Dataset-English.txt', "r") as t:
    for line in lines:
        for line in t:
            if 'Doctor' in line:
                Doctor.append(next(t))
                
                break
            
with open('COVID-Dialogue-Dataset-English.txt', "r") as f:
    for line in lines:
        for line in f:
            if 'Description' in line:
                Description.append(next(f))
                
                break

#dataset_compile = pd.DataFrame({'Description':Description, 'Patient': Patient, 'Doctor': Doctor})

sent_token1 = nltk.sent_tokenize(str(Description))
#print(sent_token1)
sent_token2 = nltk.sent_tokenize(str(Patient))
#print(sent_token1)
sent_token3 = nltk.sent_tokenize(str(Doctor))
#print(sent_token1)
dataset_tokenize = nltk.sent_tokenize(str(lines))


def greeting(text):
    text = text.lower()
    
    greetings_bot = ["hello, what's up?", "good to see you !", "hi there, how can I help?"
            "hi there!", "how are you", "hello", "howdy", "hi", "hola" ]
    from_user = ["hello", "hi", "hi there", "hi there!", "what's up", "wassup", "hey", "is anyone there?", "is anyone here?",
                 "is anyone there", "is anyone here"]
    
    for word in text.split():
        if word in from_user:
            return random.choice(greetings_bot)
 
exit_bot = ["bye", "see you later", "goodbye", "nice chatting to you, bye", "till next time", "ttyl",
            "see you!", "have a nice day", "bye!"]

def index_sort(the_list):
    length = len(the_list)
    the_list_index = list(range(0,length))

    x = the_list
    for i in range(length):
        for j in range(length):
            if x[the_list_index[i]] > x[the_list_index[j]]:
                
                swap = the_list_index[i]
                the_list_index[i] = the_list_index[j]
                the_list_index[j] = swap
                
                
    return the_list_index

def response_from_bot(user_input):
    user_input = user_input.lower()
    dataset_tokenize.append(user_input)
    
    talkie = " "
    cm = CountVectorizer().fit_transform(dataset_tokenize)
    similarity_scores = cosine_similarity(cm[-1],cm)
    similarity_scores_list = similarity_scores.flatten()
    
    index = index_sort(similarity_scores_list)
    index =  index[1:]
    
    find_response = 0
    
    f = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            talkie = talkie + "" + dataset_tokenize[index[i]]
            find_response = 1
            f = f+1
            
        if f>2:
            break
        
    if find_response==0:
        talkie = talkie +""+ random.choice([["Sorry, i did't get that","Sorry, can't understand you", 
                                             "Please give me a succint info, I don't seem to get you", "Not sure I understand"]])


    dataset_tokenize.remove(user_input)
    
    return talkie




while (True):
    user_input = input()
    if user_input.lower() in exit_bot:
        print("COVID-talkie:", random.choice(["See you!", "Have a nice day!", "Bye!, Come back again soon.",
                             "Bye!","Chat with you later!"]))
        break

    else:
        if greeting(user_input) != None:
            print("COVID-talkie:" + greeting(user_input))
            
        else:
            print("COVID-talkie:" + response_from_bot(user_input))
            
            
   













