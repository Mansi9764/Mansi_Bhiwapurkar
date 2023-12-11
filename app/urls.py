from django.urls import path
from app import views

urlpatterns = [
    path('',views.view_list_page,name='view_list_page'),
]