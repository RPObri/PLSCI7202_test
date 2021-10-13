'''Author: Ryan O'Briant'''
'''Edited by: Honghe Sun'''
'''Update date: 10/12/2021'''
'''Descrition: This script is designed to download information from websites'''

''' Utilize BeautifulSoup function from bs4 package.
Website: https://pypi.org/project/bs4/
"bs4" seems to be an alternative name of the official name "BeautifulSoup4";
To install: pip install bs4
'''
from bs4 import BeautifulSoup
'''
Website: https://docs.python-requests.org/en/latest/
Requests allows you to send HTTP/1.1 requests extremely easily.
To install: pip install requests
'''
import requests

# Set up the url address that will be retrieved.
url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C49&q=johnsongrass+sorghum+halepense&btnG=&oq=johnsongr'


'''
The variable "headers" is not defined when it was used, but I don't know what the content should be in this variable.
Then I simply remove this variable to go to the next step.
'''
# response = requests.get(url, headers=headers)
response = requests.get(url)
# print(response.text)

'''
Another error occurs at soup assignment, reporting "bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?".
I did some search online, finding that we need to install lxml. The bs4.builder.builder_registry.builders returns "[<class 'bs4.builder._htmlparser.HTMLParserTreeBuilder'>]".
However, I failed to install package lxml with pip, so I give up to fix this.
'''
import bs4
print(bs4.builder.builder_registry.builders)

#import lxml
#soup=BeautifulSoup(response.content, 'lxml')

''' I commented the following lines to leave them for further revision, and to make sure the previous commands work well.
for item in soup.select('data-lid'):
  print(item.select('h3')[0].get_text())
  print(item.select('a')[0]['href'])

  print(item.select('gs_rs')[0].get_text)
  print('-------------------')
'''
