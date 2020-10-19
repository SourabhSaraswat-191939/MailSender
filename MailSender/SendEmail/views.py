from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'index.html')


def send(request):
    if request.method == 'POST':
        message = request.POST['message']
        to = [request.POST['to']]
        html_content = render_to_string('email_template.html',{'title':'Bytecode Mail Sender','content': message})
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            "testing subject",
            text_content,
            settings.EMAIL_HOST_USER,
            to
        )
        email.attach_alternative(html_content,"text/html")
        email.send()
        return render(request,'email_sended.html')
