from django.urls import path
from app import views

urlpatterns = [
    path('',views.view_list_page,name='view_list_page'),
    path('create',views.create,name='create'),
    path('insert',views.insertData,name='insertData'),
    path('update/<id>',views.updateData,name='updateData'),
    path('delete/<id>',views.deleteData,name='deleteData'),
    path('confirmDelete/<id>',views.confirmDelete,name='confirmDelete'),

]