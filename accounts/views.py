from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse,render_to_response
from accounts.forms import UserProfileInfoForm, RegistrationForm

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfileInfo

##change password + redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

#update profile
from django.contrib.auth.models import User
from .forms import UserProfileForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

#confirmation email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.core.mail import send_mail, BadHeaderError

from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext



##########################

# def login(request):
#     form = AuthenticationForm(request)
#
#     context = {'form':form}
#     return render(request,"accounts/login.html", context)

############UPDATE PROFILE###################
@login_required
def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    user_form = UserProfileForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(User, UserProfileInfo,
        fields=('mobile', 'city','profile_picture', 'experience', 'daca' ))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()

                    messages.success(request, 'Your profile was successfully updated!')
                    return HttpResponseRedirect('')

        return render(request, "accounts/edit_profile.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied


##############CHANGE PASSWORD PROFILE PAGE#################
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect("accounts:change_password")
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
#############REGISTER##################
def register(request):
    registered = False
    if request.method == 'POST':
        # Get info from "both" form
        user_form = RegistrationForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            username = user_form.cleaned_data['username']
            first_name = user_form.cleaned_data['first_name']
            last_name = user_form.cleaned_data['last_name']
            contact_email = user_form.cleaned_data['email']
            contact_phone = profile_form.cleaned_data['mobile']
            city = profile_form.cleaned_data['city']

            user = user_form.save(commit=False)
            user.is_active = False
            user.save()
            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)
            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user
            # Check if they provided a profile picture
            if 'profile_picture' in request.FILES:
                # If yes, then grab it from the POST form reply
                profile.profile_picture = request.FILES['profile_picture']
            # Now save model
            profile.save()

            #Email to new user
            from_email = 'aabeesnc@gmail.com'
            current_site = get_current_site(request)
            subject = 'New Account with All About Bees'
            message = render_to_string('accounts/confirmation_email.html', {
                'user': first_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            })
            msg = EmailMessage(subject, message, from_email, [contact_email],)
            # user.email_user(subject, message)

            ##### Email to Bee Club #####
            name = first_name + " " + last_name
            subject = "AAB New Member Registration: " + name
            message = (
                "A new person registered as a member for All About Bees <br><br>" +
                "Name: " + name +
                "<br>Email: " + contact_email +
                "<br>Phone: " + contact_phone
                )
            from_email = 'aabeesnc@gmail.com'

            msg2 = EmailMessage(subject, message, contact_email, ['aabeesnc@gmail.com'],)
            msg2.content_subtype = "html"
            try:
                msg.send()
                msg2.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            # Registration Successful!
            registered = True
        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        # user_form = UserForm()
        user_form = RegistrationForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'accounts/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
