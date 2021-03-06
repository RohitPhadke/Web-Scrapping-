#Step 1: Import libraries for Web Scrapping
import nltk
import urllib
import bs4 as bs
import re
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
#Getting the data source
source = urllib.request.urlopen('https://en.wikipedia.org/wiki/India').read()

#Parsing the data / creating Beautiful Soup object
soup = bs.BeautifulSoup(source,'lxml')

#Fetching the data
text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text
    
#Preprocessing the data
text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)
text = re.sub(r'\s+',' ',text)
text = re.sub(r'\s+',' ',text)

#Preparing the dataset
sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentence) for sentence in sentences]