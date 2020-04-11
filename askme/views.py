from django.shortcuts import render
from .models import Question
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
	return render(request, 'index.html')

def question_list(request):
	questions = Question.objects.all()
	return render(request, 'askme/question_list.html', {'questions': questions[::-1]})

def create(request):
    if request.method == "POST":
        question = Question()
        question.question_author = request.POST.get("name")
        question.question_text = request.POST.get("question_text")
        question.save()
    return HttpResponseRedirect("/askme")