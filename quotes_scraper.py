from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.goodreads.com/quotes")

soup = BeautifulSoup(res.text, 'lxml')

quote = soup.find_all('div', {'class' : 'quoteText'})


for q in quote:
	author = q.find('a', {'class': 'authorOrTitle'})
	isSpan = q.find('script')
	if(isSpan):
		continue
	else:
		print(q.text)
		print()