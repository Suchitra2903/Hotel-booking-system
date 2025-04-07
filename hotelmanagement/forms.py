from django import forms

from hotelmanagement.models import UserRegistration


class RegisterForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1960, 2025)))

    class Meta:
        model = UserRegistration
        fields = ('firstname','email','password','mobilenumber','dob','gender','address')