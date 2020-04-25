from bs4 import BeautifulSoup
from urllib.request import urlopen

f = open("새파일.txt", 'w')

response = urlopen('https://m.zum.com/')
soup = BeautifulSoup(response, 'html.parser')
for anchor in soup.select('div ol li a'):
    anchor.span.decompose()
    data = anchor.get_text().strip()
    print(data)
    f.write(data+'\n')

f.close()
