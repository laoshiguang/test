from django.conf.urls import url, include
from api.view import account

urlpatterns = [
    url(r'^login/$', account.Login.as_view()),
    url(r'^account/$', account.Account.as_view({"get": "list", "post": "create"})),
    url(r'^account/(?P<pk>\d+)/$', account.Account.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    url(r'^accountexamine/$', account.AccountExamine.as_view()),
]
