
from django.contrib import admin
from django.conf.urls import url,include

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'login/',include('login.urls')),
    url(r'booktable/',include('BookTable.urls')),
    url(r'foodorder/',include('FoodOrder.urls')),
    url(r'about/', include('AboutUs.urls')),
    url(r'', include('Home.urls')),
]