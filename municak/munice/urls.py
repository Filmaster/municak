from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.ProduktListView.as_view(), name='list'),
    path('detail/<int:pk>', views.ProduktDetailView.as_view(), name='detail'),
]