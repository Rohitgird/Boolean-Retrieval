#!C:\Python27\python.exe

from pprint import pprint
import cgi,cgitb,collections
import os



#------------------------------Query File-------------------------------------

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
words=[]
def extract_words():
    #words=[]
    dict={}
    flag=0
    for z in file_names("./Documents//"): 
                    #words=[]
                    f = open("./Documents//"+z,'r')
                    for x in f:
                            try:
                                word = x.split()
                                word = [w.lower() for w in word]
                                words.append(word)
                            except:
                                pass

                        
    #print (words)

#Create Postings list
    
    
    for i in range(len(words)):
        for j in range(len(words[i])):
            posting_list[words[i][j].lower()].append(i+1)
            
            
    #sorted(posting_list.items(), key=lambda x: x[1])
    #print (posting_list)

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
form=cgi.FieldStorage()
query=str(form.getvalue("quer"))
#print (query)

queryTerms=[]


queryDictionary= defaultdict(list)
def execQuery(query,queryDict):
    
    queryTerms = (query).split(' ')
    queryTerms = [t.lower() for t in queryTerms]

    #print (queryTerms)
    flag = 0
    for i in range(1,len(queryTerms),2):
        if queryTerms[i].lower()!='and' or (len(queryTerms))%2==0:
            return ("Invalid Query")
            
    
    
    queryTerms[:] = [x for x in queryTerms if x.upper() != 'AND']
    #print queryTerms
    
    for term in queryTerms:
        queryDict[term]=posting_list[term]
    #print queryDict
    #print dict(queryDict)
  #  queryDict = dict(sorted(dict(queryDict), key=lambda k: len(queryDict[k]))) #Get this sorted
    #print queryDict
    queryDict['zzz']=[]

    queryDict = collections.OrderedDict(sorted(queryDict.items()))
    #print queryDict

    
    return PostingsIntersection(queryDict[list(queryDict)[0]],queryDict[list(queryDict)[1]],1,queryDict)



#------------------------------Ends Query File-------------------------------


ListStore = execQuery(query,queryDictionary)
if(execQuery(query,queryDictionary)!="Invalid Query"):
    ListStore1 = ' , '.join(str(v) for v in ListStore)
else:
    ListStore1 = "Entered Query is Invalid"

if(ListStore1==""):
    ListStore1 = "No Document Matches"



print "Content-Type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>IR Assignment 3</title>'
print '<style>#viewposting{text-decoration:none} @keyframes gradient{0%,100%{background-position:0 0}50%{background-position:100% 100%}} body{display:-webkit-flex;display:-ms-flex;display:flex;justify-content:center;-ms-align-items:center;align-items:center;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;background-color:#000;color:#fff;text-align:center;font-family:sans-serif;font-size:2em;} .bg{background:linear-gradient(to bottom right,#FF8235,#ffff1c,#92FE9D,#00C9FF,#a044ff,#e73827);background-repeat:no-repeat;background-size:1000% 1000%;animation:gradient 150s ease infinite}#finalRes{color:white; font-weight: bold;}</style>'
print '</head>'
print '<body class="bg">'
print '<h2>The resultant documents are</h2><br/>'
print "<h3><strong><span id='finalRes'>"+str(ListStore1)+"</span></strong></h3>"
print '<a href="../postingList.html" id="viewposting"><h6>View Posting List</h6></a></button><br/>'
print '</body>'
print '</html>'
