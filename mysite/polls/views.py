# Sort of front end is written here
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render
from django.http import Http404

def details(request, question_id):
    return HttpResponse("You're looking at the question %s." %question_id)

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

def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("The Question doesn't exist.")
        return render(request, 'polls/details.html', {"question": question})

