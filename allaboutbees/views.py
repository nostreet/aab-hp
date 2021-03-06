from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.models import UserProfileInfo

#email
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings
# reCAPTCHA
import urllib
import json
import urllib.request

#for getting all data necessary for the members area
@login_required
def member_area(request):
    data_list = User.objects.all().order_by('first_name')
    date_dict = {"member_area":data_list}
    return render(request,'members.html',date_dict)

#for getting the pictures from the users connected with the commitee
# @login_required
# def contact_area(request):
#     data_list = User.objects.all()
#     date_dict = {"contact_area":data_list}
#     return render(request,'contact.html',date_dict)

class MainPage(LoginRequiredMixin, TemplateView):
    template_name = 'main.html'

class MembersPage(LoginRequiredMixin, TemplateView):
    template_name = 'members.html'

class NewsPage(LoginRequiredMixin, TemplateView):
    template_name = 'news.html'

class HivewarePage(LoginRequiredMixin, TemplateView):
    template_name = 'hiveware.html'

class SuppliersPage(LoginRequiredMixin, TemplateView):
    template_name = 'suppliers.html'

class HowtoPage(LoginRequiredMixin, TemplateView):
    template_name = 'howto.html'


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                subject = form.cleaned_data['subject']
                from_email = form.cleaned_data['from_email']
                message = form.cleaned_data['message']
                subject = "Customer enquiry - All About Bees: " + subject
                try:
                    send_mail(subject, message, from_email, ['aabeesnc@gmail.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                messages.success(request, 'Success! Thank you for your message.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return redirect('home')
    return render(request, "index.html", {'form': form})
