from django.urls import path   
from Appmtv.views import familia


urlpatterns = [
    path('familia/', familia),
]