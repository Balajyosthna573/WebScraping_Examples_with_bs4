from bs4 import BeautifulSoup
import requests


#url,req,soup
url="https://balajyosthna.wixsite.com/pbjarttech"
req=requests.get(url)
soup=BeautifulSoup(req.text, "html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))

