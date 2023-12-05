from django.urls import include, path
from .import views
urlpatterns = [
    path('test', views.test, name='test'),
    
    
]