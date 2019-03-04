from django.urls import path
from .views import kane, empdetail,empdelete,emp_form,emp_update
urlpatterns=[
    path('',kane,name='kane'),
    path('empdetail/<int:pk>',empdetail, name="empdetail"),
    path('empdelete/<int:pk>',empdelete, name="empdelete"),
    path('empdetail/create',emp_form, name="emp_form"),
    path('empdetail/update/<int:pk>',emp_update, name="emp_update")

]