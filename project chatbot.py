#Import Libraries
from newspaper import Article
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import numpy as np
import warnings

#Ignore any warning messages
warnings.filterwarnings('ignore')

#Download the packages from NLTK
nltk.download('punkt',quiet=True)
nltk.download('wordnet',quiet=True)

#get the article url
article= Article('https://en.wikipedia.org/wiki/Coronavirus_disease_2019','https://twitter.com/hashtag/covid19')
article.download()
article.parse()
article.nlp()
corpus= article.text
print(corpus)

#Tokenization
text= corpus
sent_tokens=nltk.sent_tokenize(text) #convert the text into list of sentences
#print(sent_tokens)


#create a dictionary
remove_punct_dict= dict( (ord(punct),None) for punct in string.punctuation)
#print(string.punctuation)

#print the dictionary
#print(remove_punct_dict)



#create a function to return a list of lemmatized lower case words
def LemNormalize(text):
    return nltk.word_tokenize(text.lower().translate(remove_punct_dict))
#print(LemNormalize(text))


#Keyword Matching
#Greeting Inputs
greeting_inputs=["hi","hello","hola","wassup","hey"]
greeting_response=["howdy","hi","hey","hey there"]

#function to return a random response
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in greeting_inputs:
            return random.choice(greeting_response)

#generate the response
def response(user_response):
    

#user response/query
#user_response= 'what is covid-19'
    user_response= user_response.lower()

    #set the chatbot response to an empty string
    robo_response=''

    sent_tokens.append(user_response)

    #create a tfidfvectorizer object
    TfidfVec= TfidfVectorizer(tokenizer= LemNormalize, stop_words='english')

    #convert the text to a matrix of TF-IDF features
    tfidf=TfidfVec.fit_transform(sent_tokens)

    ###print the tfidf features
    #print(tfidf)

    #get the measure of (similarity scores)
    vals= cosine_similarity(tfidf[-1], tfidf)
    #print(vals)

    #Get the index of the most similar text/sentence to the users response
    idx =vals.argsort()[0][-2]

    #Reduce the dimensionality of vals
    flat= vals.flatten()

    #Sort the list in ascending order
    flat.sort()

    #get the most similar score to user response
    score= flat[-2]

    #if the variable  'score' is 0 then there is no text similar to user response
    if(score==0):
        robo_response= robo_response+"I apologize , i don't understand."
    else:
        robo_response= robo_response+sent_tokens[idx]

    #print(sent_tokens[idx])
    sent_tokens.remove(user_response)
    return robo_response



flag=True
print("DOCBot: I am DocBot. I ll answer your queries about covid-19")
while(flag==True):
    user_response=input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you'):
            flag=False
            print("DocBot: You are welcome")
        else:
            if(greeting(user_response)!=None):
                print("DocBot:"+greeting(user_response))
            else:
                print("DocBot:"+response(user_response))
                
    else:
        flag=False
        print("DocBot: Chat with you later")
        









































