from django import forms

from college import settings

MALE = "MALE"
FEMALE = "FEMALE"
OTHER = "OTHER"
DATE_INPUT_FORMATS = ['%d-%m-%Y']


class AdmissionForm(forms.Form):
    GENDER_CHOICES = [(MALE, "Male"),
                      (FEMALE, "Female"),
                      (OTHER, "Other")
                      ]
    name = forms.CharField(label="Name", required=False,
                           widget=forms.TextInput(attrs={'placeholder': "Jobi Jo", 'required': 'True'}))
    email = forms.CharField(label="Email", required=False,
                            widget=forms.EmailInput(attrs={'placeholder': "abc12@gmail.com", 'required': 'True'}))
    phone_number = forms.IntegerField(label="Phone Number", required=False, widget=forms.NumberInput(
        attrs={'placeholder': "+9197******83"}))
    dob = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, label="Date of Birth", required=False,
                          widget=forms.DateInput(
                              attrs={'required': 'True'}
                          ))
    gender = forms.CharField(label="Gender", required=False, widget=forms.RadioSelect(choices=GENDER_CHOICES))
    qualification = forms.CharField(label="Qualification", required=False,
                                    widget=forms.TextInput(attrs={'required': 'true'}))
    address = forms.CharField(label="Address", required=False, widget=forms.TextInput(attrs={'required': 'True'}))
    landmark = forms.CharField(label="Landmark", required=False, widget=forms.TextInput(attrs={'required': 'True'}))
    state = forms.CharField(label="State", required=False, widget=forms.TextInput(attrs={'required': 'True'}))
    pincode = forms.IntegerField(label="Pincode", required=False, widget=forms.NumberInput(attrs={'required': 'True'}))
    photo = forms.CharField(label="Photo", required=False, widget=forms.FileInput(attrs={'required': 'true'}))
    signature = forms.CharField(label="Signature", required=False, widget=forms.FileInput(attrs={'required': 'true'}))
    sslc = forms.CharField(label="SSLC", required=False, widget=forms.FileInput(attrs={'required': 'true'}))
    hsc = forms.CharField(label="HSC", required=False, widget=forms.FileInput(attrs={'required': 'true'}))
    aadhaar = forms.CharField(label="Aadhaar", required=False, widget=forms.FileInput(attrs={'required': 'true'}))
    community = forms.CharField(label="Community", required=False, widget=forms.FileInput(attrs={'required': 'true'}))
    transfer = forms.CharField(label="Transfer Certificate", required=False,
                               widget=forms.FileInput(attrs={'required': 'true'}))
    conduct = forms.CharField(label="Conduct Certificate", required=False,
                              widget=forms.FileInput(attrs={'required': 'true'}))
    verify = forms.BooleanField(label="I am sure above details are correct with my knowledge")


class PGAdmissionForm(AdmissionForm):
    degree_certificate = forms.FileField(label="Degree Certificate", required=False,
                                         widget=forms.FileInput(attrs={'required': 'True'}))
    provisional_certificate = forms.FileField(label="Provisional Certificate", required=False,
                                              widget=forms.FileInput(attrs={'required': 'True'}))
