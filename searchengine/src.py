from google import search

def goog(term,num):
    urls = []
    for url in search(term, tld='es', lang='es', stop=num):
        urls.append(url)
    return urls
