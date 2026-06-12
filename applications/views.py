from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from applications.constants import PAGINATION_LIMIT
from applications.forms import RequestForm, RequestStatusForm
from applications.models import Request


class RequestListView(ListView):
    queryset = Request.objects.defer('text')
    template_name = 'applications/requests.html'
    context_object_name = 'requests'
    paginate_by = PAGINATION_LIMIT


class RequestCreateView(SuccessMessageMixin, CreateView):
    form_class = RequestForm
    template_name = 'applications/request_create.html'
    success_url = reverse_lazy('applications:request_list')
    success_message = 'Заявка успешно создана'


class RequestDetailView(DetailView):
    model = Request
    template_name = 'applications/request_detail.html'
    context_object_name = 'request_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'status_form' not in context:
            context['status_form'] = RequestStatusForm(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = RequestStatusForm(request.POST, instance=self.object)
        if form.is_valid():
            form.save()
            return redirect('applications:request_detail', pk=self.object.pk)
        return self.render_to_response(self.get_context_data(status_form=form))
