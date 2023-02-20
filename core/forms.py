from django import forms

class SendNotificationForm(forms.Form):
    title = forms.CharField(max_length=128, required=True)
    notification_text = forms.CharField(max_length=256, required=True)