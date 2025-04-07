from django import forms

from hoteladmin.models import AdminModel


class AdminForm(forms.ModelForm):
    class Meta:
        model = AdminModel
        fields = ('hotelname','address','mobilenumber','roomcategory','actype','uploadimage','amount')

