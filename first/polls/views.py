from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question
from django.template import loader,RequestContext
#import logging
#logger=logging.getLogger(__name__)
def Index(request):
	latest_que = Question.objects.order_by('-date')[:5] #set
	#output = ",".join(q.que_text for q in latest_que) jitte bhi que h unko comma se jodega
	template = loader.get_template('polls/index.html')
	
	#get the data we have to pass into index .html file
	context = {
	'latest_qu':latest_que
	}
	#return HttpResponse(output)
	return HttpResponse(template.render(context,request))
	
# Create your views here.

def details(request,question_id):
# if quesion does not exist show 404 error
	a = get_object_or_404(Question,pk=question_id)
	# a= Question.objects.get(pk=question_id)                    
	template = loader.get_template('polls/details.html')
	context = {
	'a':a
	}
	#logger.debug("ANSHUL PAGal h bhot")
	#response= "the details of question {}.".format(question_id)
	return HttpResponse(template.render(context,request))
	
def result(request,question_id):
	a = get_object_or_404(Question,pk=question_id)
	# a= Question.objects.get(pk=question_id)                    
	template = loader.get_template('polls/result.html')
	context = {
	'a':a
	}
	
	return HttpResponse(template.render(context,request))
	
	
def votes(request,question_id):
	a = get_object_or_404(Question,pk=question_id)
	try:
	#request.post lets u access the submitted data like in form checkbox is named as choice so it will return the id in string .
		selected_choice= a.choice_set.get(pk=request.POST['choice'])
	except:
		return render(request,'polls/details.html',{'a':a,'error_message':"please select a choice"})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		#logger.debug(" nothing ".format(selected_choice.votes))
		#print(selected_choice.votes)
		#print(selected_choice.choice_text)
		#print(selected_choice.votes())
		# parameters of responseredirect=(destination,value that we want to pass)
		return HttpResponseRedirect(reverse('polls:result', args=(a.id,)))
		