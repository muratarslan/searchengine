# Installing RDFLib    # sudo easy_install -U "rdflib>=3.0.0" #
# http://semanticweb.org/wiki/Getting_data_from_the_Semantic_Web

#Import Graph class from the rdflib package and create a Graph instance

from rdflib import Graph, URIRef

g = Graph()

# "g" variable has empty graph now

# The graph object has a method called "parse" which allows you to give it a file name from your local system or an HTTP URI, as well as an optional format, and it will try to load data from that source. We'll load in data about Elvis Presley. 

g.parse("http://dbpedia.org/resource/Elvis_Presley")

# To see that we've loaded some data by seeing how many statements are in the graph object: 

len(g)

# So let's retrieve the birth and death dates from the graph. The first thing we need to know are the URIs of the properties. On DBpedia, the URIs used for this are:

# http://dbpedia.org/ontology/birthDate
# http://dbpedia.org/ontology/deathDate 

for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/birthDate")):
     print stmt

# The response will be as follows: 

# (rdflib.term.URIRef('http://dbpedia.org/resource/Elvis_Presley'), rdflib.term.Literal(u'1935-01-08', datatype=rdflib.term.URIRef('http://www.w3.org/2001/XMLSchema#date')))

# This is a Python tuple object. You can access the data inside it as you would a tuple, and you can call str() on the URIRef and Literal objects to return the string representation (Java users: this is basically Python's equivalent of the toString() method). 

# Birthdate
for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/birthDate")):
    print "the person represented by", str(stmt[0]), "was born on", str(stmt[1])

# Spouse
for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/spouse")):
    print "the person represented by", str(stmt[0]), "was married to", str(stmt[1])


# As was noted earlier, this graph structure is a big bucket where you can throw as much data as you like (within the limits of your computer's memory, of course). So let's test our birth date query with a few more people. 

g.parse("http://dbpedia.org/resource/Tim_Berners-Lee")
g.parse("http://dbpedia.org/resource/Albert_Einstein")
g.parse("http://dbpedia.org/resource/Margaret_Thatcher")


for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/birthDate")):
     print "the person represented by", str(stmt[0]), "was born on", str(stmt[1])

# And we should get this in response: 

#the person represented by http://dbpedia.org/resource/Tim_Berners-Lee was born on 1955-06-08
#the person represented by http://dbpedia.org/resource/Margaret_Thatcher was born on 1925-10-13
#the person represented by http://dbpedia.org/resource/Elvis_Presley was born on 1935-01-08
#the person represented by http://dbpedia.org/resource/Albert_Einstein was born on 1879-03-14




