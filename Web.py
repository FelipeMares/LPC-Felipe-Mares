import requests
from bs4 import BeautifulSoup
url_page = 'https://www.uanl.mx/enlinea/'
page = requests.get(url_page).text
print(page)

