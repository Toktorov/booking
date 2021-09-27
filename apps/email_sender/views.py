from django.views.generic import CreateView
from apps.email_sender.models import MessageSender
from apps.email_sender.forms import MessageSenderForm
from apps.email_sender.tasks import send_message_to_email
from django.urls import reverse_lazy



class MessageSenderCreateView(CreateView):
    model = MessageSender
    form_class = MessageSenderForm
    success_url = reverse_lazy('country_index')

    def form_valid(self, form):
        form.save()
        send_message_to_email.delay(form.instance.email)
        return super().form_valid(form)