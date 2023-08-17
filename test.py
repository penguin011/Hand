import requests
from bs4 import BeautifulSoup
  
URL = "https://jp.mercari.com/item/m39159070677"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())