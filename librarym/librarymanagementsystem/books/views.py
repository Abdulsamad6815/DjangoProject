from django.shortcuts import render,redirect
from books.models import Library


# Create your views here.
def add(request):
    if (request.method=='POST'):
        book_name_ = request.POST['book_name']
        author_name_ = request.POST['author_name']
        price_ = request.POST['price']
        type_of_book_ = request.POST['type_of_book']



        insert_data=Library.objects.create(book_name=book_name_,author_name=author_name_,price=price_,type_of_book=type_of_book_)
        insert_data.save()
        return redirect('/')
    return render(request,'books/add.html')


def index(request):
    content={}
    #content['data']=Library.objects.all()
    content['data']=Library.objects.filter(is_deleted='n')

    return render(request,'books/index.html',content)


def delete(request,tid):
    record_to_be_deleted= Library.objects.filter(id=tid)
    #record_to_be_deleted.delete()
    record_to_be_deleted.update(is_deleted='y')
    return redirect('/')

def update(request,tid):
    if (request.method=='POST'):
        book_name_ = request.POST['book_name']
        author_name_ = request.POST['author_name']
        price_ = request.POST['price']
        type_of_book_ = request.POST['type_of_book']

        records_to_be_update = Library.objects.filter(id=tid)

        records_to_be_update.update(book_name=book_name_,author_name=author_name_,price=price_,type_of_book=type_of_book_)
        return redirect('/')
    else:
        content={}
        content['data']=Library.objects.get(id=tid)

        return render(request,'books/update.html',content)
