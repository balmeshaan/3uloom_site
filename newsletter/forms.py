from django import forms


class ContactForms(forms.Form):
    name = forms.CharField(required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    subject = forms.CharField(required=True, label='Subject')
    message = forms.CharField(widget=forms.Textarea, required=True)


class TutorForm(forms.Form):
    tutor_name = forms.CharField(required=True, label='Name')

    tutor_subject = forms.CharField(required=True, label='Subject')
    tutor_level = forms.IntegerField(required=True, label='Level')
    tutor_email = forms.EmailField(required=True,  label='Email')


class StudentForm(forms.Form):
    student_name = forms.CharField(required=True, label='Name')
    student_age = forms.IntegerField(required=True, label='Age')
    student_email = forms.EmailField(required=True,  label='Email')

