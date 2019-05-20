from django.conf.urls import url,include
from . import views


urlpatterns=[
    url(r'proceed/', views.proceed),
    url(r'forgot/',views.forgot),
    url(r'logout/',views.logout),
    url(r'verify/',views.verify),
    url(r'register/',views.RegisterUser),
    url(r'login/',views.login),
    url(r'',views.login),
]