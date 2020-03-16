from django.views.generic import TemplateView
from newsletter.forms import ContactForms, StudentForm, TutorForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.shortcuts import redirect
from newsletter.models import ContactFormInfo, TutorContactFormInfo, MessageContactFormInfo


class MainView(TemplateView):
    template_name = 'newsletter/index.html'

    def get(self, request, *args, **kwargs):
        question_form = StudentForm(self.request.GET or None)
        answer_form = TutorForm(self.request.GET or None)
        message_contact_form = ContactForms(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context['student_form'] = question_form
        context['tutor_form'] = answer_form
        context['message_contact_form'] = message_contact_form
        return self.render_to_response(context)

    def post(self, request, **kwargs):
        Contact_Form = StudentForm
        if request.method == 'POST':
            form = Contact_Form(data=request.POST)
            tutor_form = TutorForm(request.POST)
            message_form = ContactForms(request.POST)
            if form.is_valid():
                student_name = request.POST.get('student_name')
                student_age = request.POST.get('student_age')
                student_email = request.POST.get('student_email')

                template = get_template('newsletter/student_form.txt')
                context = {
                    'student_name': student_name,
                    'student_age': student_age,
                    'student_email': student_email,
                }

                content = template.render(context)

                email = EmailMessage(
                    "New contact form email",
                    content,
                    "Creative web" + '',
                    ['3uloomkw@gmail.com'],
                    headers={'Reply To': student_email}
                )

                email.send()

                p = ContactFormInfo(student_name=student_name, student_age=student_age, student_email=student_email)
                p.save()
            elif tutor_form.is_valid():
                tutor_name = request.POST.get('tutor_name')
                tutor_subject = request.POST.get('tutor_subject')
                tutor_level = request.POST.get('tutor_level')
                tutor_email = request.POST.get('tutor_email')

                template = get_template('newsletter/contact_form.txt')
                context = {
                    'tutor_name': tutor_name,
                    'tutor_subject': tutor_subject,
                    'tutor_level': tutor_level,
                    'tutor_email': tutor_email
                }

                content = template.render(context)

                email = EmailMessage(
                    "New contact form email",
                    content,
                    "Creative web" + '',
                    ['3uloomkw@gmail.com'],
                    headers={'Reply To': tutor_email}
                )

                email.send()
                p = TutorContactFormInfo(tutor_name=tutor_name, tutor_subject=tutor_subject, tutor_level=tutor_level,tutor_email=tutor_email)
                p.save()
            elif message_form.is_valid():

                name = request.POST.get('name')
                mail = request.POST.get('email')
                subject = request.POST.get('subject')
                message = request.POST.get('message')

                template = get_template('newsletter/contact_forms.txt')
                context = {
                    'name': name,
                    'email': mail,
                    'subject': subject,
                    'message': message
                }

                content = template.render(context)

                email = EmailMessage(
                    "New contact form email",
                    content,
                    "Creative web" + '',
                    ['3uloomkw@gmail.com'],
                    headers={'Reply To': mail}
                )

                email.send()
                p = MessageContactFormInfo(name=name, subject=subject, message=message,
                                         email=mail)
                p.save()
            else:

                print("nothing")

        response = redirect('/')
        return response
