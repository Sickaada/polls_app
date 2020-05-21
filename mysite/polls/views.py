# Sort of front end is written here
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question,options

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-published_date')[:5]

class DetailsView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def votes_count(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    context = {
        'question': question,
        'error_message': "You didn't select a choice."
    }
    try:
        selected_option = question.options_set.get(pk=request.POST['options'])
    except(KeyError,options.DoesNotExist):
# Redisplaying the question voting form
        return render(request, 'polls/details.html', context )
    else:
        selected_option.votes_count += 1
        selected_option.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))





