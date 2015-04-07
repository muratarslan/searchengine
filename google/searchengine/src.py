from google import search

def goog(term,num):
	for url in search(term, tld='es', lang='es', stop=num):
		print(url)
