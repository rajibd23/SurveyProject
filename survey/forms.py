from django import forms
from .models import Question

FORM_CHOICES= [
    ('yes', 'Yes'),
    ('no', 'No'),
]

class FirstForm(forms.Form):

    widget = forms.RadioSelect(choices=FORM_CHOICES)
    comment = forms.CharField(widget=forms.Textarea)

class SecondForm(forms.Form):
    latest_questions = Question.objects.order_by('id')
    q3_choice = [
        (0,'Medicine procurement'),
        (1, 'Grocery'),
        (2, 'Doctor Appointment'),
        (3, 'Local transport'),
        (4, 'Other Utilities'),
    ]
    q4_choice = [
        (0, 'Yes'),
        (1, 'No'),
    ]
    q7_choice = [
        (0,'Have fulltime help'),
        (1, 'Thru Whatsapp'),
        (2, 'Thru Friends'),
        (3, 'Home Delivery'),
        (4, 'Self'),
    ]
    q9_choice = [
        (0,'Daily'),
        (1, 'Weekly'),
        (2, 'Monthly'),
        (3, 'Never'),
        (4, 'Are you interested?'),
    ]
    q13_choice = [
        (0,'Health monitoring'),
        (1, 'Doctor appointment'),
        (2, 'Medicine procurement'),
        (3, 'Grocery Procurement'),
        (4, 'Emotional support'),
        (5, 'local transport'),
        (6, 'Other utilities'),
        (7, 'Video conferencing'),
        (8, 'All services'),
    ]
    q15_choice = [
        (0,'Rs. 3000 to Rs. 5000'),
        (1, 'Rs. 5000 to Rs. 7000'),
        (2, 'Rs. 7000 to Rs. 10000'),
    ]
    name = forms.CharField(label='Your Name :', max_length=100, error_messages={'required': 'Please enter your name'})
    email = forms.EmailField(label='Your Email Id :', error_messages={'required': 'Please enter your email id'})

    for question in latest_questions:
        if question.seq == 2:
            q2 = forms.CharField(label=question.question_text+' :', max_length=100, error_messages={'required': 'Please enter city'})
        elif question.seq == 3:
            q3 = forms.MultipleChoiceField(
            choices=q3_choice,
            initial='0',
            widget=forms.SelectMultiple(),
            required=True,
            label=question.question_text+' :',
        )
        elif question.seq == 4:
            q4 = forms.CharField(label=question.question_text+' :', widget=forms.RadioSelect(choices=q4_choice))
        elif question.seq == 5:
            q5 = forms.CharField(label=question.question_text+' :', widget=forms.RadioSelect(choices=q4_choice))
        elif question.seq == 6:
            q6 = forms.CharField(label=question.question_text+' :', max_length=200, error_messages={'required': 'Please enter'})
        elif question.seq == 7:
            q7 = forms.MultipleChoiceField(
            choices=q7_choice,
            initial='0',
            widget=forms.SelectMultiple(),
            required=True,
            label=question.question_text+' :',
        )
        elif question.seq == 8:
            q8 = forms.CharField(label=question.question_text+' :', widget=forms.RadioSelect(choices=q4_choice))
        elif question.seq == 9:
            q9 = forms.MultipleChoiceField(
            choices=q9_choice,
            initial='0',
            widget=forms.SelectMultiple(),
            required=True,
            label=question.question_text+' :',
        )
        elif question.seq == 10:
            q10 = forms.CharField(label=question.question_text+' :', widget=forms.RadioSelect(choices=q4_choice))
        elif question.seq == 11:
            q11 = forms.CharField(label=question.question_text+' :', widget=forms.RadioSelect(choices=q4_choice))
        elif question.seq == 12:
            q12 = forms.CharField(label=question.question_text+' :', widget=forms.RadioSelect(choices=q4_choice))
        elif question.seq == 13:
            q13 = forms.MultipleChoiceField(
            choices=q13_choice,
            initial='0',
            widget=forms.SelectMultiple(),
            required=True,
            label=question.question_text+' :',
        )
        elif question.seq == 14:
            q14 = forms.CharField(label=question.question_text+' :', widget=forms.Textarea())
        elif question.seq == 15:
            q15 = forms.MultipleChoiceField(
            choices=q15_choice,
            initial='0',
            widget=forms.SelectMultiple(),
            required=True,
            label=question.question_text+' :',
        )
