from django.urls import path
from employee import views


urlpatterns=[
    path("reg",views.IndexView.as_view()),
    path("login",views.LoginView.as_view())
]