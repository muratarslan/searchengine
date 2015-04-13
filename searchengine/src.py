from google import search
from rdflib import Graph, URIRef
from SPARQLWrapper import SPARQLWrapper, JSON
from django.http import Http404

def goog(term,num):
	if term:
		urls = []
		for url in search(term, tld='es', lang='en', stop=num):
			urls.append(url)
		return urls
	else:
		raise Http404

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
	th = []
	g = Graph()
	g.parse("http://dbpedia.org/resource/" + term)
	for thumb in g.subject_objects(URIRef("http://dbpedia.org/ontology/thumbnail")):
		th = thumb[1]
	return th

def birthName(term):
	sparql = SPARQLWrapper("http://dbpedia.org/sparql")
	sparql.setQuery("""
    		PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    		SELECT ?bname WHERE {<http://dbpedia.org/resource/%s>
                         <http://dbpedia.org/ontology/birthName> ?bname .
   		 }
	"""%(term))

	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	try:
		bname = results.values()[1]['bindings'][0]['bname']['value']
	except IndexError:
		bname = ()

	return bname



def location(term):
	sparql = SPARQLWrapper("http://dbpedia.org/sparql")
	sparql.setQuery("""
    		PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    		SELECT ?loc WHERE {<http://dbpedia.org/resource/%s>
                         <http://dbpedia.org/property/location> ?loc .
   		 }
	"""%(term))

	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	try:
		loc = results.values()[1]['bindings'][0]['loc']['value']
	except IndexError:
		loc = ()

	return loc

def population(term):
	sparql = SPARQLWrapper("http://dbpedia.org/sparql")
	sparql.setQuery("""
    		PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    		SELECT ?pop WHERE {<http://dbpedia.org/resource/%s>
                         <http://dbpedia.org/ontology/populationTotal> ?pop .
   		 }
	"""%(term))

	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	try:
		pop = results.values()[1]['bindings'][0]['pop']['value']
	except IndexError:
		pop = ()

	return pop

def elevation(term):
	sparql = SPARQLWrapper("http://dbpedia.org/sparql")
	sparql.setQuery("""
    		PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    		SELECT ?ele WHERE {<http://dbpedia.org/resource/%s>
                         <http://dbpedia.org/ontology/elevation> ?ele .
   		 }
	"""%(term))

	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	try:
		ele = results.values()[1]['bindings'][0]['ele']['value']
	except IndexError:
		ele = ()

	return ele

def postalCode(term):
	sparql = SPARQLWrapper("http://dbpedia.org/sparql")
	sparql.setQuery("""
    		PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    		SELECT ?post WHERE {<http://dbpedia.org/resource/%s>
                         <http://dbpedia.org/ontology/postalCode> ?post .
   		 }
	"""%(term))

	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	try:
		post = results.values()[1]['bindings'][0]['post']['value']
	except IndexError:
		post = ()

	return post

def areaCode(term):
	sparql = SPARQLWrapper("http://dbpedia.org/sparql")
	sparql.setQuery("""
    		PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    		SELECT ?area WHERE {<http://dbpedia.org/resource/%s>
                         <http://dbpedia.org/ontology/areaCode> ?area .
   		 }
	"""%(term))

	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	try:
		area = results.values()[1]['bindings'][0]['area']['value']
	except IndexError:
		area = ()

	return area

	



