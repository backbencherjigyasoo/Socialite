from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', RedirectView.as_view(url='dashboard/')),
]
