from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    #path("<int:id>",views.book_detail, name="book-detail")
    # bitno da dodje prije jer će biti konflikata!
    path("products/", views.products, name="products"),
    path("<slug:slug>",views.book_detail, name="book-detail"),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    
]
