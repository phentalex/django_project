from django.urls import path

from applications.views import (
    RequestCreateView,
    RequestDetailView,
    RequestListView
)

app_name = 'applications'

urlpatterns = [
    path('create/', RequestCreateView.as_view(), name='request_create'),
    path('<int:pk>/', RequestDetailView.as_view(), name='request_detail'),
    path('', RequestListView.as_view(), name='request_list'),
]
