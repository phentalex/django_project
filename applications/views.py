from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from applications.forms import RequestForm
from applications.models import Request


class RequestListView(ListView):
    queryset = Request.objects.defer('text')
    template_name = 'applications/requests.html'
    context_object_name = 'requests'


class RequestCreateView(SuccessMessageMixin, CreateView):
    form_class = RequestForm
    template_name = 'applications/request_create.html'
    success_url = reverse_lazy('applications:request_list')
    success_message = 'Заявка успешно создана'
