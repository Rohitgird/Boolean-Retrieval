from collections import defaultdict
''' Instructions:
Place this extract.py program outside the folder with the 10 text files named 1.txt... 10.txt
Preferably follow the same path, else change the path name accordingly.
The extracted words from all the 10 documents is present in the list "words[]"
This array can be used for the posting list creation'''
import os
def file_names(mypath):
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    return onlyfiles

from collections import defaultdict
''' Instructions:
Place this extract.py program outside the folder with the 10 text files named 1.txt... 10.txt
Preferably follow the same path, else change the path name accordingly.
The extracted words from all the 10 documents is present in the list "words[]"
This array can be used for the posting list creation'''
import os
def file_names(mypath):
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    return onlyfiles

posting_list=defaultdict(list)
#Extract Words

def extract_words():
    words=[]
    dict={}
    flag=0
    for z in file_names("C:\\Apache24\\cgi-bin\\Documents\\"): 
                    #words=[]
                    f = open("C:\\Apache24\\cgi-bin\\Documents\\"+z,'r')
                    for x in f:
                            try:
                                word = x.split()
                                #print words
                                words.append(word)
                            except:
                                pass

                        
    print (words)

#Create Postings list
    
    
    for i in range(len(words)):
        for j in range(len(words[i])):
            #if(words[i][j] not in posting_list):
            posting_list[words[i][j]].append(i+1)
                 
            #else:
                #posting_list[words[i][j]].append(i+1)

            print posting_list[words[i][j]]    
            
    #sorted(posting_list.items(), key=lambda x: x[1])
    print (posting_list)

extract_words() #To extract words, and then create a postings list from them

#Intersection of 2 postings
def intersection(p1,p2):
    s1=set(p1)
    
    s2=set(p2)
    
    s = set.intersection(s1,s2)
    
    return list(s)

#Postings Intersection List
def PostingsIntersection(p1,p2,id,queryDict):
    
    if p2!=[]:
        p = intersection(p1,p2)
        return PostingsIntersection(p,queryDict[list(queryDict)[id+1]],id+1,queryDict)
    else:
        return p1
                             
#Query

query = raw_input("Enter AND Query")
print (query)

queryTerms=[]



def execQuery(query):
    queryDict = defaultdict(list)
    queryTerms = (query).split(' ')
    #print (queryTerms)
    flag = 0
    for i in range(1,len(queryTerms),2):
        if queryTerms[i].lower()!='and' or (len(queryTerms))%2==0:
            print ("Invalid Query")
            flag=1
            break
    if flag==0:           
        print ("Successful")
    
    queryTerms[:] = [x for x in queryTerms if x.upper() != 'AND']
    #print queryTerms
    
    for term in queryTerms:
        queryDict[term]=posting_list[term]
    #print queryDict
    print dict(queryDict)
  #  queryDict = dict(sorted(dict(queryDict), key=lambda k: len(queryDict[k]))) #Get this sorted
    #print queryDict
    queryDict['Extra']=posting_list['cdsddcsdfv']
    print queryDict

    
    print PostingsIntersection(queryDict[list(queryDict)[0]],queryDict[list(queryDict)[1]],1,queryDict)

execQuery(query)=defaultdict(list)
#Extract Words

def extract_words():
    words=[]
    dict={}
    flag=0
    for z in file_names("C:\\Apache24\\cgi-bin\\Documents\\"): 
                    #words=[]
                    f = open("C:\\Apache24\\cgi-bin\\Documents\\"+z,'r')
                    for x in f:
                            try:
                                word = x.split()
                                #print words
                                words.append(word)
                            except:
                                pass

                        
    print (words)

#Create Postings list
    
    
    for i in range(len(words)):
        for j in range(len(words[i])):
            #if(words[i][j] not in posting_list):
            posting_list[words[i][j]].append(i+1)
                 
            #else:
                #posting_list[words[i][j]].append(i+1)

            print posting_list[words[i][j]]    
            
    #sorted(posting_list.items(), key=lambda x: x[1])
    print (posting_list)

extract_words() #To extract words, and then create a postings list from them

#Intersection of 2 postings
def intersection(p1,p2):
    s1=set(p1)
    
    s2=set(p2)
    
    s = set.intersection(s1,s2)
    
    return list(s)

#Postings Intersection List
def PostingsIntersection(p1,p2,id,queryDict):
    
    if p2!=[]:
        p = intersection(p1,p2)
        return PostingsIntersection(p,queryDict[list(queryDict)[id+1]],id+1,queryDict)
    else:
        return p1
                             
#Query

query = raw_input("Enter AND Query")
print (query)

queryTerms=[]



def execQuery(query):
    queryDict = defaultdict(list)
    queryTerms = (query).split(' ')
    #print (queryTerms)
    flag = 0
    for i in range(1,len(queryTerms),2):
        if queryTerms[i].lower()!='and' or (len(queryTerms))%2==0:
            print ("Invalid Query")
            flag=1
            break
    if flag==0:           
        print ("Successful")
    
    queryTerms[:] = [x for x in queryTerms if x.upper() != 'AND']
    #print queryTerms
    
    for term in queryTerms:
        queryDict[term]=posting_list[term]
    #print queryDict
    print dict(queryDict)
  #  queryDict = dict(sorted(dict(queryDict), key=lambda k: len(queryDict[k]))) #Get this sorted
    #print queryDict
    queryDict['Extra']=posting_list['cdsddcsdfv']
    print queryDict

    
    print PostingsIntersection(queryDict[list(queryDict)[0]],queryDict[list(queryDict)[1]],1,queryDict)

execQuery(query)