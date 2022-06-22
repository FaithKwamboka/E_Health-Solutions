from django.urls import re_path
from . import views


app_name = "hospital" 


urlpatterns=[
    re_path('^$',views.landingpage,name = 'landingpage'),
]

