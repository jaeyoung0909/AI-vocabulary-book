# I use word frequency data from http://www.wordfrequency.info

from urllib.request import urlopen
from bs4 import BeautifulSoup 


# save word frequency ranked 4001 - 5000 words as 'freqWords'
def crawler():
    html = open("Word frequency_ based on 450 million word COCA corpus.htm", "r")
    bsObject = BeautifulSoup(html, 'html.parser')

    trs = bsObject.find_all('table', id='table1')[1].find_all('tr')[4:]
    f = open('freqWord.txt','w')
    for tr in trs:
        tds = tr.find_all('td')
        if int(tds[0].get_text()) > 4000:
            f.write(tds[1].get_text() + '\n')
