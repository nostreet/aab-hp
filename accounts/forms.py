from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm

###############################
from django.contrib.auth.forms import AuthenticationForm
###############################
from django.forms.widgets import CheckboxSelectMultiple

class MyAuthenticationForm(AuthenticationForm):
    class Meta():
        model = User
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:

            if self.user_cache is None:
                try:
                    user_temp = User.objects.get(username=username)
                except:
                    user_temp = None

                if user_temp is not None:
                        self.confirm_login_allowed(user_temp)
                else:
                    raise forms.ValidationError(
                        self.error_messages['invalid_login'],
                        code='invalid_login',
                        params={'username': self.username_field.verbose_name},
                    )

        return self.cleaned_data

###############################
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email',]

###############################
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True,max_length=30)
    last_name = forms.CharField(required=True,max_length=30)
    email = forms.EmailField(required=True,max_length=75)

    class Meta:
        model = User
        fields = ("username","first_name", "last_name", "email",)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

###############################
class UserForm(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        widgets = {'password': forms.PasswordInput(),}
        fields = ('username','email','first_name', 'last_name','password',)

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

class UserProfileInfoForm(forms.ModelForm):
    mobile = forms.CharField(min_length=6,required=True,
            widget=forms.TextInput(attrs={'class':'form-control' ,
            'autocomplete': 'off','pattern':'[0-9]+', 'title':'Enter numbers Only '}))

    class Meta():
        model = UserProfileInfo
        fields = ('profile_picture','mobile','city', 'experience', 'daca')

    def __init__(self, *args, **kwargs):
        super(UserProfileInfoForm, self).__init__(*args, **kwargs)
        self.fields['experience'].label = "How long have you been beekeeping?"
        self.fields['daca'].label = "Do you have a DECA?"
