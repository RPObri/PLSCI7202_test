from bs4 import BeautifulSoup
import requests


url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C49&q=johnsongrass+sorghum+halepense&btnG=&oq=johnsongr'

response = requests.get(url, headers=headers)

soup=BeautifulSoup(response.content, 'lxml')

for item in soup.select('data-lid'):
  print(item.select('h3')[0].get_text())
  print(item.select('a')[0]['href'])

  print(item.select('gs_rs')[0].get_text)
  print('-------------------')
