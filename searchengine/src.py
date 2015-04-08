from google import search
from rdflib import Graph, URIRef

def goog(term,num):
    urls = []
    for url in search(term, tld='es', lang='es', stop=num):
        urls.append(url)
    return urls

def showRdf(term):
	stmts = []
	g = Graph()
	g.parse("http://dbpedia.org/resource/" + term)
	for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/birthDate")):
		stmts.append(stmt)
		print stmts
	return stmts



