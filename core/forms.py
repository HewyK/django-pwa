from django import forms

class SendNotificationForm(forms.Form):
    notification_text = forms.CharField(max_length=256, required=True)