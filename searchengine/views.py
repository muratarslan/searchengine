from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from src import *
from django.views.decorators.csrf import csrf_exempt

# For verification error
@csrf_exempt

def search(request):
	if request.method == 'POST':

		result = goog(request.POST['term'], 3)

		rdf_birth   = list(birth(request.POST['term']))
		rdf_death = list(death(request.POST['term']))
		rdf_desc   = list(description(request.POST['term']))

                b = {}
		d = {}
		desc = {}

		# Birth Date
                if len(rdf_birth) > 0:
                    b.update({'link': unicode(rdf_birth[0][0]), 'birth_date': unicode(rdf_birth[0][1])})
                print b

		# Death Date
		if len(rdf_death) > 0:
                    d.update({'link': unicode(rdf_death[0][0]), 'death_date': unicode(rdf_death[0][1])})
                print d

		# Spouse
		if len(rdf_desc) > 0:
                    desc.update({'desc': unicode(rdf_desc[0][1])})
                print desc
	


		return render(request,'search.html', {'result': result, 
									      'birth_dict': b, 
									      'death_dict':d,
									      'desc_dict':desc,
									      'term': request.POST['term']})
	return render(request,'search.html')


