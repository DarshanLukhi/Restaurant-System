from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required

from . import views




urlpatterns=[
    url(r'done/',views.done),
    url(r'proceed/',views.proceed),
    url(r'',views.BookTable),
]