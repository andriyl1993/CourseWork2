from django.conf.urls import include, url
from django.contrib import admin

from main.views import index_view, login_view, logout, count_clients_view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index_view, name="index"),
    url(r'^login/', login_view, name="login"),
    url(r'^logout/', logout, name="logout"),
    # url(r'^register/', register_view, name="register"),
    url(r'^count-clients/', count_clients_view, name="count-clients"),
]
