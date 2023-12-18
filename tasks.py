# First task in the NLP textDecipher 

import nltk
# nltk.download('all')
# from nltk import word_tokenize, sent_tokenize

import scipy

# print("First Statement of the project")

name = input('Enter the text\n')    

method = input('Enter the task\n')

def outFromMethod(name, method):
    # print(name)
    # print(method)
    if method == "NLTK":

        wt = nltk.word_tokenize(name)
        st = nltk.sent_tokenize(name)
    
        return (wt, st)

print(outFromMethod(name, method)) 