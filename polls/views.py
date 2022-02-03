from ast import arg
from ssl import HAS_TLSv1_1
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
# Create your views here.

def index(request):
    latest_question_list = Question.objects.all()
    return render(request, 'polls/index.html', {
        'lastest_question_list': latest_question_list
        })

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    value = question.choice_set.all()
    return render(request, 'polls/detail.html', {
        'question':question,
        'value': value
    })

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def detail_redirect(request, slug):
    question = Question.objects.get(pk=slug)
    value = question.choice_set.all()
    redirect_path = HttpResponseRedirect(reverse('detail_redirect', args=[value]))

