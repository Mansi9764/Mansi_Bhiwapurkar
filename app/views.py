from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.utils import timezone
 

def view_list_page(request):
    data=Contact.objects.all()
    context={"data":data}
    return render(request,"list_page.html",context)


