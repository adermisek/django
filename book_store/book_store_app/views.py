from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Book, Product
from django.db.models import Avg, Max, Min, Count, Sum
from .forms import ProductForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    num_of_books = books.count()
    avg_year = books.aggregate(Avg("year"))
    oldest_book = books.aggregate(min_year=Min("year"))
    return render(request,
                  "book_store_app/index.html", 
                  {"books":books, 
                   "total_num_of_books":num_of_books,
                   "avg_year":avg_year,
                    "min_year": oldest_book['min_year']
                    })

def book_detail(request, slug):
    book = get_object_or_404(Book,slug=slug)
    return render(request,"book_store_app/book_detail.html", {
        "title":book.title,
        "author":book.author,
        "year":book.year,
        "is_bestseller":book.is_bestselling})


def products(request):
    products = Product.objects.all()
    max_price = products.aggregate(Max("price"))
    min_price = products.aggregate(Min("price"))
    products_count = products.aggregate(Count("id"))
    total_price_available = products.filter(is_available=True).aggregate(Sum("price"))["price__sum"]
    for product in products:
        product.total_price = product.quantity * product.price
    return render(request, "book_store_app/products.html", 
                  {"products": products, 
                   "max_price":max_price,
                   "min_price":min_price,
                   "products_count":products_count,
                   "total_price_available":total_price_available,
                   })



def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')  # Promijeni u naziv tvoje stranice s popisom proizvoda
    else:
        form = ProductForm(instance=product)
    return render(request, 'book_store_app/edit_product.html', {'form': form, 'product': product})

