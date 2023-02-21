from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from core.forms import *
from core.azure_notify import *
from pwa_webpush import send_user_notification

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

            # isDebug = True
            # connection_string = 'Endpoint=sb://keeplNotificationHubNamespace-test.servicebus.windows.net/;SharedAccessKeyName=DefaultFullSharedAccessSignature;SharedAccessKey=8orbRUAKOctpAlzRRahiU0NfZ2YXVOLfMfcWD60fw9c='
            # hub_name = 'keeplNotificationHub-test'
            # alert_payload = {
            #         'data':
            #             {
            #                 'msg': form.cleaned_data['notification_text']
            #             }
            #     }

            # hub = AzureNotificationHub(connection_string, hub_name, isDebug)
            # hub.send_google_notification(payload=alert_payload, is_direct=False)



            # # You can still use .filter() or any methods that return QuerySet (from the chain)
            # device = FCMDevice.objects.all().first()
            # # send_message parameters include: message, dry_run, app
            # device.send_message(Message(title="title", body="text", image="url"),
            #     topic="Optional topic parameter: Whatever you want",)

            icon_url = '/static/images/icons/icon-72x72.png'
            payload = {"head": form.cleaned_data['title'],
                       "body": form.cleaned_data['notification_text'],
                       "icon": "https://cdnkeepltest.azureedge.net/static/assets/img/keepl-white-transparent.png",
                       "url": "https://keepl-test.azurewebsites.net"}

            print('current user: ', request.user)

            send_user_notification(user=request.user, payload=payload, ttl=1000)
            # Here in the user parameter, a user object should be passed
            # The user will get notification to all of his subscribed browser. A user can subscribe many browsers.


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

