# Sort of front end is written here
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import Http404



def results(request,question_id):
    return HttpResponse("You're looking at the result of question %s." %question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on the question %s." %question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-published_date')[:5]
    
    # following key will be rendered as value
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request,'polls/index.html', context)

def details(request, question_id):
#   try:
#       question = Question.objects.get(pk = question_id)
#   except Question.DoesNotExist:
#       raise Http404("The Question doesn't exist.")
#    return render(request, 'polls/details.html', {"question": question})'''
# Using the try and except block can couple the model layer and view layer
    question = get_object_or_404(Question, pk = question_id )
    return render(request, 'polls/details.html', {'question': question})
