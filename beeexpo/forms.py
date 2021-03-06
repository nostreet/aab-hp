from django import forms
from django.core.validators import RegexValidator
from visitors.models import SignedUp

class NewSignUpForm(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(
            attrs={
                'placeholder': 'Your first name'
            }))
    last_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(
            attrs={
                'placeholder': 'Your last name',
            }))
    contact_email = forms.EmailField(required=True, max_length=150, widget= forms.EmailInput(
            attrs={'placeholder':'Your email address'}))
    contact_phone = forms.CharField(required=True,max_length=13, min_length=9,
            widget=forms.TextInput(attrs={
                'class':'form-control' , 'pattern':'[0-9]+',
                 'title':'Enter numbers Only.',
                 'placeholder': 'Your phone number'
             }))

    # TICKET_CHOICES1 = (('sat-early-130', 'Saturday $130',), ('sunday-early-150', 'Sunday $150',),('students-early-75', 'Students $75 (must have student ID)',),)
    # single_day_pass= forms.ChoiceField(widget=forms.RadioSelect, choices=TICKET_CHOICES1, required=False)
    #
    # TICKET_CHOICES2 = (('saturday-sunday-early-260', 'Saturday & Sunday $260',), ('students-weekend-early-150', 'Students $150 (must have student ID)',),)
    # weekend_pass= forms.ChoiceField(widget=forms.RadioSelect, choices=TICKET_CHOICES2, required=False)

    # TICKET_CHOICES1_normal = (('sat-150', 'Saturday $90',), ('sunday-180', 'Sunday $90',),('students-75', 'Students $75 (must have student ID)',),)
    # single_day_pass_normal= forms.ChoiceField(widget=forms.RadioSelect, choices=TICKET_CHOICES1_normal, required=False)

    TICKET_CHOICES1_normal = (('sat-150', 'Saturday $90',), ('students-75', 'Students $75 (must have student ID)',),)
    single_day_pass_normal= forms.ChoiceField(widget=forms.RadioSelect, choices=TICKET_CHOICES1_normal, required=False)

    # TICKET_CHOICES2_normal = (('saturday-sunday-350', 'Saturday & Sunday $150',), ('students-150', 'Students $150 (must have student ID)',),)
    # weekend_pass_normal= forms.ChoiceField(widget=forms.RadioSelect, choices=TICKET_CHOICES2_normal, required=False)

    CHOICES = (('yes', 'Yes',), ('no', 'No',),)
    beeclub_asso= forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=True)

    which_club = forms.CharField(required=False, max_length=150, widget=forms.TextInput(
            attrs={
                'placeholder': 'Your answer'
            }))
    CHOICES2 = (('my bee club', 'My bee club',), ('email newsletter', 'Email newsletter',),
                ('word of mouth', 'Word of mouth',), ('facebook', 'Facebook',),
                ('advertsment', 'Advertsment',),('other', 'Other',),)
    event= forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES2, required=False)

    # lunch= forms.CharField(widget=forms.CheckboxInput, required=False)

    dietary = forms.CharField(required=False, max_length=150, widget=forms.TextInput(
            attrs={
                'placeholder': 'Your dietary restrictions'
            }))

    # student = forms.CharField(widget=forms.CheckboxInput, required=False)
    mailchimp_list = forms.CharField(widget=forms.CheckboxInput, required=False)

    class Meta:
        model= SignedUp
        fields= ["first_name", "last_name", "contact_email", "contact_phone", "single_day_pass_normal",
                "beeclub_asso", "which_club", "event","dietary", ]

    def __init__(self, *args, **kwargs):
        super(NewSignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name*"
        self.fields['last_name'].label = "Last Name*"
        self.fields['contact_email'].label = "E-mail Address*"
        self.fields['contact_phone'].label = "Phone Number*"
        # self.fields['single_day_pass'].label = "Single Day Pass - Early Bird Sale (Ends 15 June 2019)"
        # self.fields['weekend_pass'].label = "Weekend Pass - Early Bird Sale (Ends 15 June 2019)"
        self.fields['single_day_pass_normal'].label = "Single Day Pass"
        # self.fields['weekend_pass_normal'].label = "Weekend Pass"
        self.fields['beeclub_asso'].label = "Are you a member of a bee club or association?*"
        self.fields['which_club'].label = "If yes, which club?"
        self.fields['event'].label = "How did you hear about this event?"
        self.fields['dietary'].label = "Ticket price includes lunch, morning and afternoon tea, if you have any dietary restrictions let us know:"
        self.fields['mailchimp_list'].label = "Tick here to receive information on bee related events"

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(
            attrs={
                'placeholder': 'Your name',
            }))
    contact_email = forms.EmailField(required=True, max_length=150, widget= forms.EmailInput(
            attrs={'placeholder':'Your email address'}))
    contact_phone = forms.CharField(required=True,max_length=12, min_length=6,
        widget=forms.TextInput(attrs={
        'class':'form-control' , 'pattern':'[0-9]+',
         'title':'Enter numbers Only ',
         'placeholder': 'Your phone number'}))
    CHOICES = (('Visiting', 'Visiting',), ('Exhibiting', 'Exhibiting',), ('Other', 'Other',))
    interest= forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=True)
    questions = forms.CharField(
        required=True,
        widget=forms.Textarea(
                attrs={'placeholder':'Your enquiry'}))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Name:"
        self.fields['contact_email'].label = "E-mail Address:"
        self.fields['contact_phone'].label = "Phone Number:"
        self.fields['interest'].label = "I am interested in:"
        self.fields['questions'].label = "Questions:"

# class TicketForm(forms.Form):
#     first_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Your first name'
#             }))
#     last_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Your last name',
#             }))
#     contact_email = forms.EmailField(required=True, max_length=150, widget= forms.EmailInput(
#             attrs={'placeholder':'Your email address'}))
#     contact_phone = forms.CharField(required=True,max_length=13, min_length=9,
#             widget=forms.TextInput(attrs={
#                 'class':'form-control' , 'pattern':'[0-9]+',
#                  'title':'Enter numbers Only.',
#                  'placeholder': 'Your phone number'
#              }))
#
#     CHOICES = (('yes', 'Yes',), ('no', 'No',),)
#     beeclub_asso= forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=True)
#     which_club = forms.CharField(required=False, max_length=150, widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Your answer'
#             }))
#     CHOICES2 = (('my bee club', 'My bee club',), ('email newsletter', 'Email newsletter',),
#                 ('word of mouth', 'Word of mouth',), ('facebook', 'Facebook',),
#                 ('advertsment', 'Advertsment',),('other', 'Other',),)
#     event= forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES2, required=False)
#
#     lunch= forms.CharField(widget=forms.CheckboxInput, required=False)
#
#     dietary = forms.CharField(required=False, max_length=150, widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Your answer'
#             }))
#
#     def __init__(self, *args, **kwargs):
#         super(TicketForm, self).__init__(*args, **kwargs)
#         self.fields['first_name'].label = "First Name*"
#         self.fields['last_name'].label = "Last Name*"
#         self.fields['contact_email'].label = "E-mail Address*"
#         self.fields['contact_phone'].label = "Phone Number*"
#         self.fields['beeclub_asso'].label = "Are you a member of a bee club or association?*"
#         self.fields['which_club'].label = "If yes, which club?"
#         self.fields['event'].label = "How did you hear about this event?"
#         self.fields['lunch'].label = "Add optional catered lunch ($12)"
#         self.fields['dietary'].label = "Dietary restrictions:"
