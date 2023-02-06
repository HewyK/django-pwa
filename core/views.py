from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from core.forms import *

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add code to return context data

        return context


class SendNotificationView(TemplateView):
    template_name = 'send_notification.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add code to return context data
        context['form'] = SendNotificationForm()

        return context

def Notify(request):

    if request.method == 'POST':
        print('post received')

        form = SendNotificationForm(request.POST)

        if form.is_valid():
            print('valid form')

            print('Notification: ', form.cleaned_data['notification_text'])

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

