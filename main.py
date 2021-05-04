import nltk
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize


# nltk.download()
# introduce english stop words
stopwords.words('english')
response = urllib.request.urlopen('http://php.net/')
html = response.read()
# remove html tags
soup = BeautifulSoup(html, "html5lib")
text = soup.get_text(strip=True)
# tokenization
tokens = text.split()
# remove stop words in tokens
clean_tokens = list()
sr = stopwords.words('english')
for token in tokens:
    if token not in sr:
        clean_tokens.append(token)
# get word frequency
freq = nltk.FreqDist(clean_tokens)
# print word frequency
for key, val in freq.items():
    print(str(key) + ':' + str(val))


if __name__ == '__main__':
    # plot 20 most frequent words
    freq.plot(20, cumulative=False)
