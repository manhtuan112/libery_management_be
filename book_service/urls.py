from django.urls import path
from book_service.views import create_book, update_book, get_book, get_all_book, delete_book
urlpatterns = [
    path('add_book/', create_book, name="add_book"),
    path('update_book/<int:id>/', update_book, name="update_book"),
    path('get_book/<int:id>/', get_book, name="get_book"),
    path('get_all_book/', get_all_book, name="get_all_book"),
    path('delete_book/<int:id>/', delete_book, name="delete_book"),




]
