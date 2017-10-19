from django.conf.urls import url
from django.contrib import admin
from habrparser.views import Parser

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'$', Parser.as_view())
]
