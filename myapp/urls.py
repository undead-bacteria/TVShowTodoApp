from django.urls import path
from .views import *

urlpatterns = [
  path('', ShowListView.as_view(), name='show_list'),
  path('show/<int:pk>/', ShowDetailView.as_view(), name='show_detail'),
  path('show/new/', ShowCreateView.as_view(), name='show_create'),
  path('show/<int:pk>/edit/', ShowUpdateView.as_view(), name='show_update'),
  path('show/<int:pk>/delete/', ShowDeleteView.as_view(), name='show_delete'),
]
