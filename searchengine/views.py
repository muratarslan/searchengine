from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from src import *
from django.views.decorators.csrf import csrf_exempt

# For verification error
@csrf_exempt

def search(request):
	if request.method == 'POST':
		result = goog(request.POST['term'], 3)
		rdf = showRdf(request.POST['term'])[0]
		#print "RESULT: %s" % result
		return render(request,'search.html', {'result': result,'rdf': rdf})
	return render(request,'search.html')


