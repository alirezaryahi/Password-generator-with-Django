from django.urls import path
from .views import generate_pass, show_pass

urlpatterns = [
    path('', generate_pass, name='generate-pass'),
    path('show-pass', show_pass, name='show-pass')
]
