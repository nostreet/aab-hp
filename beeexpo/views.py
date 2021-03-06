from .forms import ContactForm, NewSignUpForm
from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
# add to your views

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from marketing.utils import Mailchimp


# reCAPTCHA
import urllib
import json
import urllib.request

# from .forms import TicketForm

def showSignUpform(request):
    if request.method == 'GET':
        form = NewSignUpForm()
    else:
        form = NewSignUpForm(request.POST)
        if form.is_valid():

            # ''' Begin reCAPTCHA validation '''
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
            # ''' End reCAPTCHA validation '''


            if result['success']:
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                contact_email = form.cleaned_data['contact_email']
                contact_phone = form.cleaned_data['contact_phone']
                # single_day_pass = form.cleaned_data['single_day_pass']
                # weekend_pass = form.cleaned_data['weekend_pass']
                single_day_pass_normal = form.cleaned_data['single_day_pass_normal']
                # weekend_pass_normal = form.cleaned_data['weekend_pass_normal']
                beeclub_asso = form.cleaned_data['beeclub_asso']
                which_club = form.cleaned_data['which_club']
                event = form.cleaned_data['event']
                dietary = form.cleaned_data['dietary']
                mailchimp_list = form.cleaned_data['mailchimp_list']

                form.save()

                ##### Email to Bee Club #####
                name = first_name + " " + last_name
                subject = "Bee Conference Registration: " + name
                message = (
                    "A new person signed up for the Bee Conference!! <br><br>" +
                    "Name: " + name +
                    "<br>Email: " + contact_email +
                    "<br>Phone: " + contact_phone +
                    # "<br>Single day pass - early bird: " + single_day_pass +
                    # "<br>Weekend pass - early bird: " + weekend_pass +
                    "<br>Single day pass - normal (new prices now: $90 or $75 for students): " + single_day_pass_normal +
                    # "<br>Weekend pass - normal (new prices now: $150 or $150 for students): " + weekend_pass_normal +
                    "<br><br>Member of a bee club or association? " + beeclub_asso +
                    "<br>Which? " + which_club +
                    "<br><br>How did you hear about this event? " + event +
                    "<br>Dietary restrictions: " + dietary
                    )
                from_email = 'aabeesnc@gmail.com'

                msg = EmailMessage(subject, message, contact_email, ['aabeesnc@gmail.com'],)
                msg.content_subtype = "html"

                ##### Email to Person who signs up #####
                subject2 = "Bee Conference Registration for: " + name

                message2 = ("Hi")
                amount = "0"

                # if len(single_day_pass) > 0:
                #     if single_day_pass == "sat-early-130":
                #         amount = "130"
                #     elif single_day_pass == "sunday-early-150":
                #         amount = "150"
                #     else:
                #         amount = "75"
                # if len(weekend_pass) > 0:
                #     if weekend_pass == "saturday-sunday-early-260":
                #         amount = "260"
                #     else:
                #         amount = "150"
                if len(single_day_pass_normal) > 0:
                    if single_day_pass_normal == "sat-150":
                        amount = "90"
                    elif single_day_pass_normal == "sunday-180":
                        amount = "90"
                    else:
                        amount = "75"
                # if len(weekend_pass_normal) > 0:
                #     if weekend_pass_normal == "saturday-sunday-350":
                #         amount = "150"
                #     else:
                #         amount = "150"

                message2 = (
                    "Hi " + first_name + """, <br><br> Thanks for registering
                    for the South Island Bee Conference 2019. To receive your
                    ticket, you’ll need to complete the payment to:<br>
                    All About Bees North Canterbury<br>
                    38-9018-0224011-01<br>
                    Amount: $"""+ amount + """<br><br>
                    Please use your full name as the reference. Once payment
                    is received, you’ll be emailed your ticket.<br><br>
                    If you haven't received your ticket two days prior to the conference,
                    please contact aabeesnc@gmail.com <br><br>
                    Thanks and we’ll see you there.
                    """)

                msg2 = EmailMessage(subject2, message2, from_email, [contact_email],)
                msg2.content_subtype = "html"
                if mailchimp_list == "True":
                    try:
                        #Mailchimp sign up
                        Mailchimp().add_email(contact_email)
                        #send mails
                        msg.send()
                        msg2.send()
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                else:
                    try:
                        #send mails
                        msg.send()
                        msg2.send()
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                messages.success(request, "Thank you for registering to the Bee Conference. An email confirmation with more details has been sent to you.")
                return redirect('beeexpo:tickets')
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('beeexpo:tickets')
    return render(request, "beeexpo/get_tickets.html", {'form': form })

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():

            # ''' Begin reCAPTCHA validation '''
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
            # ''' End reCAPTCHA validation '''


            if result['success']:
                name = form.cleaned_data['name']
                contact_email = form.cleaned_data['contact_email']
                contact_phone = form.cleaned_data['contact_phone']
                interest = form.cleaned_data['interest']
                questions = form.cleaned_data['questions']

                subject = "AAB Contact Form enquiry: " + name
                message = (
                    "From: " + name +
                    "<br>Email: " + contact_email +
                    "<br>Phone: " + contact_phone +
                    "<br>Interested in: " + interest +
                    "<br><br> Message: " + questions
                    )
                from_email = 'aabeesnc@gmail.com'

                msg = EmailMessage(subject, message, contact_email, ['aabeesnc@gmail.com'],)
                msg.content_subtype = "html"
                try:
                    msg.send()
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                messages.success(request, 'Success! Thank you for your message.')
                return redirect('beeexpo:contact')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return redirect('beeexpo:contact')
    return render(request, "beeexpo/contact_form.html", {'form': form})
