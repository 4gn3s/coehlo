from BeautifulSoup import BeautifulSoup
import urllib
import re
import random

url = 'http://www.goodreads.com/author/quotes/566.Paulo_Coelho'
file_pointer = urllib.urlopen(url)
html_obj = BeautifulSoup(file_pointer)
quotes = []
divs = html_obj.findAll('div')
for div in divs:
    try:
        if div['class'] == u"quoteText":
            quote = div.contents[0]
            quotes.append(re.split('[;&]',quote)[2])
    except:
        continue


def GetQuote():
    return random.choice(quotes)
