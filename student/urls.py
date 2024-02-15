from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("home/",views.home),
    path("add-std/",views.std_add),
    path("delete-std/<int:rollno>",views.delete_std),
    path("update-std/<int:rollno>",views.update_std),
    path("do-update-std/<int:rollno>",views.do_update_std),
]