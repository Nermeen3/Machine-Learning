# grabs all html files in folder locations

from glob import glob
import codecs

# first data file you sent
filenames = glob("C:/Users/ninaz/Desktop/upwork/NLP Task/Data/1/*.html") # change files directory and end it with /*.html
filenames+= glob("C:/Users/ninaz/Desktop/upwork/NLP Task/Data/2/*.html")
filenames+= glob("C:/Users/ninaz/Desktop/upwork/NLP Task/Data/3/*.html")
filenames+= glob("C:/Users/ninaz/Desktop/upwork/NLP Task/Data/4/*.html")
filenames+= glob("C:/Users/ninaz/Desktop/upwork/NLP Task/Data/5/*.html")

# second data file you sent
filenames2= glob("C:/Users/ninaz/Desktop/upwork/NLP Task/Dat/2015/*.html")
filenames2= glob("C:/Users/ninaz/Desktop/upwork/NLP Task/Dat/2016/*.html")
filenames2= glob("C:/Users/ninaz/Desktop/upwork/NLP Task/Dat/2017/*.html")
print(filenames) # this line is optional jsut to show the files names
print(len(filenames))

dataframe = [codecs.open(f, 'r', 'utf-8') for f in filenames]

# extracts only text from html files and eliminates all html tags

from bs4 import BeautifulSoup as soup

# here im only implementing the code for the first html file since it will take too much time if you want to loop through all
# of the them and if you will use the loop I highly recommend that you eliminate some files or pick one folder at a time

#for file in dataframe:
containers = soup(dataframe[10].read()).get_text()  
clean_file = open('clean_file.csv', 'w+')  # creates the file if it doesnt exist
for container in containers:
    clean_file.write(container)
clean_file.close()
clean_file_occurrances = open('clean_file_occurrances.csv', 'w')

# getting all synonyms of specific words using wordnet library from nltk and store unique words in dictionary
# this library automatically generates variances and relevant words to any string you give it then add them to dictionary

from nltk.corpus import wordnet
synonyms = {}
for vsyn in wordnet.synsets("high"):
    for l in vsyn.lemmas():
        synonyms[l.name()] = 0
for vsyn in wordnet.synsets("competition"):
    for l in vsyn.lemmas():
        synonyms[l.name()] = 0
for vsyn in wordnet.synsets("technology"):
    for l in vsyn.lemmas():
        synonyms[l.name()] = 0

print('all found synonyms: ', synonyms)

# searching through the new clean csv file created for synonyms and if found increment to the synonyms dictionary
import re

clean_file = open('clean_file.csv', 'r')

high_comp_counter = 0       # optional
technolog_comp_counter = 0  # optional

# this part will search for the phrases in the clean text file created and print the whole sentence where it was found
#  here as well as store it in the created file "clean_file_occurrances"
for line in clean_file.readlines():
    if line.strip() != '':
        for word in synonyms:
            if word in line:
                synonyms[word]+= 1
                print(line)
                clean_file_occurrances.write(line)
        if re.search(r"high\w* competit\w+", line.lower()):       # optional; I added search because synonyms dictionary
            print(line)                                           # doesn't have all variances like :
            high_comp_counter+= 1                                 # "competitive", "technological",,,,
            clean_file_occurrances.write(line)                                 
            
        if re.search(r"technolog\w* competit\w+", line.lower()):  # optinal; 
            print(line)                                           
            technolog_comp_counter+= 1                            
            clean_file_occurrances.write(line)                    
    
clean_file_occurrances.close()
clean_file.close()

# prining the occurrances of synonyms that had appeared in the dataset more than zero times from the dictionary

for word in synonyms:
    if synonyms[word] != 0:
        print('occurrances of ', word, ': ', synonyms[word])

# these are optional and uncommment them if you want to use the "search" method i used above

#print("total occurrances of high competition and it's variances: ", high_comp_counter)
#print("total occurrances of technology competition and it's variances: ", technolog_comp_counter)
