from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.utils import timezone
 

def view_list_page(request):
    data=Contact.objects.all()
    context={"data":data}
    return render(request,"list_page.html",context)


def create(request):
    return render(request,"create.html")

def insertData(request):
    if request.method=="POST":
        button_clicked=request.POST.get('button')
        if button_clicked=='cancel':
            return render('/')
        else:
            name=request.POST.get("name")
            email=request.POST.get("email")
            notes=request.POST.get("notes")
            time = timezone.now()
            data=Contact.objects.all()
            if Contact.objects.filter(name=name).exists():
                messages.error(request, 'Username already exists')
                return render(request,"create.html") 
            else:
                print(name,email,notes,time)
                query=Contact(name=name,email=email,notes=notes,time=time)
                query.save()  
                data=Contact.objects.all()
                context={"data":data}
                messages.info(request,"Data inserted successfully")
                return render(request,"list_page.html",context) 
            
def updateData(request,id):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        notes=request.POST.get("notes")
        editStudent = Contact.objects.get(id=id)
        editStudent.name=name
        editStudent.email=email
        editStudent.notes=notes
        print("request objected",name,email,notes)
        print("NEW UPDATED OBJECT:",editStudent.id,editStudent.name,editStudent.email,editStudent.notes,editStudent.time)
        editStudent.save()
        print("updated successfully")
        return redirect("/")
    else:
        print("Id------",id)
        data = Contact.objects.get(id=id)
        context={"data":data}
        return render(request,"edit.html",context)