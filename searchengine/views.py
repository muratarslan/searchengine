from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from src import *
from django.views.decorators.csrf import csrf_exempt

# For verification error
@csrf_exempt

def search(request):
	if request.method == 'POST':
		result = goog(request.POST['term'], 3)
		rdf_list = list(showRdf(request.POST['term']))
                d = {}
                if len(rdf_list) > 0:
                    d.update({'link': unicode(rdf_list[0][0]), 'birth_date': unicode(rdf_list[0][1]) })
                print d

		return render(request,'search.html', {'result': result,'rdf_dict': d, 'term': request.POST['term']})
	return render(request,'search.html')


