from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import request

from django.http import HttpResponse
from django.template import loader, RequestContext
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from . import forms
from .models import Question, SurveyResponse, NoSurveyResponse
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
    form = forms.SecondForm()
    # When user is submitting the survey form
    if request.method == 'POST':
        form = forms.SecondForm(request.POST)

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
            status = ''
            html = 'Thank you for your survey!!!'
        #    return render(request, 'survey/thankyou.html', {'html': html, 'form': form,'message':messages})
        # When is_valid() failed
        else:
            form.fields['name'].widget.attrs.update({'class':"form-control"})
            form.fields['email'].widget.attrs.update({'class':"form-control"})
            form.fields['q2'].widget.attrs.update({'class':"form-control"})
            form.fields['q3'].widget.attrs.update({'class':"form-control"})
            form.fields['q6'].widget.attrs.update({'class':"form-control"})
            form.fields['q7'].widget.attrs.update({'class':"form-control"})
            form.fields['q9'].widget.attrs.update({'class':"form-control"})
            form.fields['q13'].widget.attrs.update({'class':"form-control"})
            form.fields['q14'].widget.attrs.update({'class':"form-control"})
            form.fields['q15'].widget.attrs.update({'class':"form-control"})
            html = 'Welcome to the survey'
            status = 'failure'

        return render(request, 'survey/detail.html', {'html': html, 'status': status,'form': form})
    # User comes for the 1st time to the Survey form
    else:
        html = 'Welcome to the survey'
        status = 'new'
        return render(request, 'survey/detail.html', {'html': html, 'form': form, 'status': status})
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
    name = request.POST.get("name")

    email = request.POST.get("email")

    comment = request.POST.get("comment")

    if name != "" and email !="":
    #try:
        if selected_choice == '2':
            form2 = forms.SecondForm()

            form2.fields['name'].widget.attrs.update({
                'value': name, 'class':"form-control"
            })
            form2.fields['email'].widget.attrs.update({
                'value': email, 'class':"form-control"
            })
            form2.fields['q2'].widget.attrs.update({
              'class':"form-control"
            })
            form2.fields['q3'].widget.attrs.update({
              'class':"form-control"
            })
            form2.fields['q6'].widget.attrs.update({
              'class':"form-control"
            })
            form2.fields['q7'].widget.attrs.update({
              'class':"form-control"
            })
            form2.fields['q9'].widget.attrs.update({
              'class':"form-control"
            })
            form2.fields['q13'].widget.attrs.update({
              'class':"form-control"
            })
            form2.fields['q14'].widget.attrs.update({
              'class':"form-control"
            })
            form2.fields['q15'].widget.attrs.update({
              'class':"form-control"
            })
            html = 'Welcome to the survey'
            status = 'new'

            return render(request, 'survey/detail.html', {'html': html, 'form': form2,'status':status})
            #return HttpResponseRedirect(reverse('survey:detail',))
        else:
            if request.method == 'POST':
                mdl = NoSurveyResponse.objects.create(name=name,
                                                      emailid=email,
                                                      comments=comment)
                mdl.save()
                html = 'Thank you for your survey!!!'
                return render(request, 'survey/thankyou.html', {'html': html, 'name': name})
            else:
                html = 'There is some issue with the Survey. Sorry!!!'
                return render(request, 'survey/thankyou.html', {'html': html, 'name': name})
    else:
        html = 'Welcome to the survey - Blank'
        latest_questions = Question.objects.order_by('id')
        error_name = ""
        error_email = ""
        if name == "":
            error_name = 'Name is a required field.'
        if email == "":
            error_email = 'Email is required.'
        status = 'new'
        return render(request, 'survey/index.html', {'html': html, 'latest_questions': latest_questions,'error_name':error_name, 'error_email':error_email,'status':status})

    #except:
    #    return render(request, 'survey/thankyou.html', {'error_message': "Please select a choice2"})
    #else:
     #   return render(request, 'survey/thankyou.html', {'error_message': "Please select a choice3"})


