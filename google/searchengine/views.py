from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from src import *
from django.views.decorators.csrf import csrf_exempt

# For verification error
@csrf_exempt

def search(request):

    if request.method == 'POST':
	return render(request,'search.html', {'result': goog(request.POST['term'], 3)})
	#return HttpResponseRedirect("/")
	print "Olur Abi"
    else:
	print "Sicar Abi"	
	return render(request,'search.html')
	
