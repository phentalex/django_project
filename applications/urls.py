from django.urls import path

from applications.views import RequestCreateView, RequestListView

app_name = 'applications'

urlpatterns = [
    path('create/', RequestCreateView.as_view(), name='request_create'),
    path('', RequestListView.as_view(), name='request_list'),
]
