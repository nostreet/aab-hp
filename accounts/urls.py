from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from .forms import MyAuthenticationForm

app_name = 'accounts'

urlpatterns=[

    url(r'^register/$', views.register,name='register'),
    url(r"logout/$", LogoutView.as_view(), name="logout"),
    # url(r'^login/$', views.login,name='user_login'),
    # url(r'^login/$',auth_views.login,{'template_name': 'accounts/login.html', 'authentication_form': MyAuthenticationForm},name='login'),
    url(r'^login/$',auth_views.login,{'template_name': 'accounts/login.html'},name='login'),
    ############################
    url(r'^update/(?P<pk>[\-\w]+)/$', views.edit_user, name='edit_profile'),
    url(r'^change_password/$', views.change_password, name="change_password"),
    ##############################
    url(r'^reset_password/$',
        PasswordResetView.as_view(template_name='accounts/password_reset_form.html',
        success_url=reverse_lazy('accounts:password_reset_done'),
        email_template_name='accounts/password_reset_email.html',
        subject_template_name='accounts/password_reset_subject.txt'),
        name='password_reset'),

    url(r'^reset_password/done/$',
        PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),

    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',
        success_url = reverse_lazy('accounts:password_reset_complete')),
        name='password_reset_confirm'),

	url(r'^reset/complete/$',
        PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),
]
