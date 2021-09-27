from django import forms
from apps.email_sender.models import MessageSender


class MessageSenderForm(forms.ModelForm):

    class Meta:
        model = MessageSender
        fields = ['email']