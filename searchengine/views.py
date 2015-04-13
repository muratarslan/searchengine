from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from src import *
import re
from django.views.decorators.csrf import csrf_exempt


# For verification error
@csrf_exempt



def search(request):
	if request.method == 'POST':
		
		result = goog(modify(request.POST['term']), 3)
		rdf_birth   = list(birth(modify(request.POST['term'])))
		rdf_death = list(death(modify(request.POST['term'])))
		rdf_desc   = list(description(modify(request.POST['term'])))
		rdf_thumb = thumbnail(modify(request.POST['term']))
		rdf_bname = birthName(modify(request.POST['term']))

                brth      = {}
		dth       = {}
		desc     = {}
		thumb  = {}
		bname = {}

		# Birth Date
                if len(rdf_birth) > 0:
                    brth.update({'link': unicode(rdf_birth[0][0]), 'birth_date': unicode(rdf_birth[0][1])})
                print brth

		# Death Date
		if len(rdf_death) > 0:
                    dth.update({'link': unicode(rdf_death[0][0]), 'death_date': unicode(rdf_death[0][1])})
                print dth

		# Description
		if len(rdf_desc) > 0:
                    desc.update({'desc': unicode(rdf_desc[0][1])})
                print desc

		# Thumb
		if len(rdf_thumb) > 0:
                    thumb.update({'thumb': unicode(rdf_thumb)})
                print thumb

		# Birth Name
		if len(rdf_bname) > 0:
                    bname.update({'bname': unicode(rdf_bname)})
                print bname

		# Child
		#if len(rdf_thumb) > 0:
                #    child.update({'child': unicode(rdf_child[0][1])})
                #print child
	


		return render(request,'search.html', {'result': result, 
									      'birth_dict': brth, 
									      'death_dict':dth,
									      'desc_dict':desc,
									      'thumb_dict':thumb,
									      'bname_dict':bname,
									      'term': request.POST['term']})
	return render(request,'search.html')

def modify(s):
     s = re.sub(r"[^\w\s]", '', s) #non-word characters
     s = re.sub(r"\s+", '_', s)     # replace ' ' to '_'
     return s.title()


