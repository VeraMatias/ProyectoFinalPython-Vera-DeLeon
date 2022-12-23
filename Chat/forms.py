from django import forms
from django.contrib.auth.models import User


class ChatForm(forms.Form):
    receptor = forms.ModelChoiceField(queryset=User.objects.all().order_by('username').exclude(id=1))
    mensaje = forms.CharField(max_length=1200)

    #def __init__(self, user, *args, **kwargs):
    #    super(ChatForm, self).__init__(*args, **kwargs)
    #    #self.fields['used_his'].queryset = User.objects.filter(pk = user.id)
    #    self.fields['receptor'].queryset = User.objects.filter(id = user.id)