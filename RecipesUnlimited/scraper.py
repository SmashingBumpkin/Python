import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.bbcgoodfood.com/user/23650/recipe/millies-cookies-recipe')
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text # gets you the text of the <title>(...)</title>
print(title)
body = soup.head.text
print(len(body))