from django.shortcuts import render , redirect , get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        ooo = BookForm(request.POST , request.FILES)
        if ooo.is_valid():
            ooo.save()


        hopa = CategoryForms(request.POST)    
        if hopa.is_valid():
            hopa.save()  




    context = {
        'aaaa' :Books.objects.all(),
        'category': Category.objects.all(),
        'forms': BookForm(),
        'categoryies' : CategoryForms(),
        'allbooks' : Books.objects.filter(active=True).count(),
        'booksold' : Books.objects.filter(status='sold').count(),
        'bookrented' : Books.objects.filter(status='rented').count(),
        'bookavailable' : Books.objects.filter(status='available').count(),
    }
    
    return render(request , 'pages/index.html' , context=context)

def books(request):
    context = {
        'aaaa' :Books.objects.all(),
        'category': Category.objects.all()
    }
    return render(request , 'pages/books.html', context=context)

def delete(request , id):
    book_delete = get_object_or_404(Books , id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/lms/index')
    return render(request , 'pages/delete.html')

def update(request , id):
    book_id = Books.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST , request.FILES , instance=book_id)
        if book_save.is_valid():
           book_save.save()
           return redirect('/lms/index')
    else:
        book_save = BookForm(instance=book_id) 
    context = {
        'form' : book_save
    }          
    return render(request , 'pages/update.html' , context=context)