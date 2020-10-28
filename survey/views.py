from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import request

from django.http import HttpResponse
from django.template import loader, RequestContext
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from . import forms
from .models import Question, SurveyResponse
from . forms import FirstForm
from . forms import SecondForm

# Create your views here.
def index(request):
    form = FirstForm()

    if request.method == 'POST':
        form = FirstForm(request.POST)
        html = 'we have recieved this form again'
    else:
        form = FirstForm()
        latest_questions = Question.objects.order_by('id')
        context = {'latest_questions': latest_questions}
    return render(request, 'survey/index.html', context)
    #return render(request, 'signup.html', {'html': html, 'form': form})



def detail(request):

    if request.method == 'POST':
        form = forms.SecondForm(request.POST)
        print(form['q4'].value)
        if form.is_valid():

            mdl = SurveyResponse.objects.create(name=form.cleaned_data['name'], emailid=form.cleaned_data['email'],
                                                city=form.cleaned_data['q2'],question1=form.cleaned_data['q4'],
                                                question2=form.cleaned_data['q5'],question3=form.cleaned_data['q6'],
                                                question4=form.cleaned_data['q7'],question5=form.cleaned_data['q3'],
                                                question6=form.cleaned_data['q8'],question7=form.cleaned_data['q9'],
                                                question8=form.cleaned_data['q10'],question9=form.cleaned_data['q11'],
                                                question10=form.cleaned_data['q12'],question11=form.cleaned_data['q13'],
                                                question12=form.cleaned_data['q15'],comments=form.cleaned_data['q14'])
        mdl.save()
        html = 'Thank you for your survey!!!'
    else:
        html = 'Welcome to the survey'
    return render(request, 'survey/detail.html', {'html': html, 'form': form})
    #return render(request, 'survey/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'survey/results.html', {'question' : question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request, 'survey/detail.html', {'question': question,'error_message': "Please select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('survey:results', args=(question.id,)))

def needSurvey(request):
    selected_choice = request.POST.get("choice")
    print(selected_choice)
    #try:
    if selected_choice == '2':
        return HttpResponseRedirect(reverse('survey:detail',))
    else:
        return render(request, 'survey/thankyou.html', {'error_message': "Please select a choice2"})
    #except:
    #    return render(request, 'survey/thankyou.html', {'error_message': "Please select a choice2"})
    #else:
     #   return render(request, 'survey/thankyou.html', {'error_message': "Please select a choice3"})

