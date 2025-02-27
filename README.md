# 📚 Book Store App

Book Store App is a Django-based web application for managing books and products in a bookstore. It allows users to browse books, edit product details, and view basic statistics like minimum and maximum prices.

## 🚀 Features
- Display all books and products
- View detailed information about each book
- Edit product details
- View statistics (e.g., highest and lowest product prices)

## 📂 Project Structure

book_store_app/ 
│── templates/book_store_app/ # HTML templates (frontend) 
│── models.py # Database models 
│── views.py # Backend logic 
│── forms.py # Django forms 
│── urls.py # URL configuration 
│── apps.py # App settings


#  Key Routes (URLs)
Route	Description
/	Homepage with a list of books
/book/<slug>/	Detailed book view
/products/	List of all products
/edit-product/<int:id>/	Edit a product


 ## Technologies Used
Python & Django (backend)
Bootstrap (frontend styling)
SQLite (database)
