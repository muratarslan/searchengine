from google import search
from rdflib import Graph, URIRef

def goog(term,num):
    urls = []
    for url in search(term, tld='es', lang='es', stop=num):
        urls.append(url)
    return urls

def birth(term):
	g = Graph()
	g.parse("http://dbpedia.org/resource/" + term)
	birth = g.subject_objects(URIRef("http://dbpedia.org/ontology/birthDate"))
	return birth

def death(term):
	g = Graph()
	g.parse("http://dbpedia.org/resource/" + term)
	death = g.subject_objects(URIRef("http://dbpedia.org/ontology/deathDate"))
	return death

def description(term):
	g = Graph()
	g.parse("http://dbpedia.org/resource/" + term)
	desc = g.subject_objects(URIRef("http://dbpedia.org/property/description"))
	return desc


def thumbnail(term):
	g = Graph()
	g.parse("http://dbpedia.org/resource/" + term)
	for thumb in g.subject_objects(URIRef("http://dbpedia.org/ontology/thumbnail")):
		th = thumb[1]
	return th



