from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

from .models import Books

# Create your views here.


def show(request):
        books =Books.objects.all()
        return render(request, 'show.html', {'books': books})

        
@login_required
def insert(request):
    if request.method =="POST":
        
        id=request.POST.get('id')
        book_name=request.POST.get('name')
        publish_date=request.POST.get('publish_date')
        author=request.POST.get('author')
        
        book_info=Books(id=id, book_name=book_name, publish_date=publish_date, author=author)
        book_info.save()
        return redirect('/')

    else:
        
        return render(request, 'index.html')


@login_required
def delete(request, id):
    books = Books.objects.get(id=id)
    books.delete()
    return redirect('/')


@login_required
def update(request, id):
    
    books=Books.objects.get(id=id)
    return render(request, 'update.html', {'books':books})

def index(request): 
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginuser(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(username,password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/index")
        else:
            return render(request, 'login.html')
            # No backend authenticated the credentials
        
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")