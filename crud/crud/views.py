from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import *
def index(request):
    return render(request, 'crud/index.html', {})

def registerpage(request):
    return render(request, 'crud/insert.html')

def save(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        image=request.FILES['image']    
        gender=request.POST.get('gender')

        data=register(name=name,email=email,contact=contact,image=image,gender=gender)
        data.save()
        return redirect(fetch)
    else:
        return render(request, 'crud/insert.html')

def fetch(request):
    obj = register.objects.all()
    return render(request, 'crud/fetch.html', {'data': obj})

def edit(request,id):
    a=register.objects.get(id=id)
    return render(request,'crud/edit.html',{'a':a})

def update(request,id):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        image=request.FILES['image']    
        gender=request.POST.get('gender')

        data=register(id=id,name=name,email=email,contact=contact,image=image,gender=gender)
        data.save()
        return redirect(fetch)
    else:
        return render(request, 'crud/fetch.html')

def delete(request, id):
    a = register.objects.get(id=id)
    a.delete()
    return redirect(fetch)
