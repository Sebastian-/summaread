from django.urls import path

from .views import BookListView, CreateBookView, EditBookView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('create/', CreateBookView.as_view(), name='create_book'),
    path('edit/<int:pk>', EditBookView.as_view(), name='edit_book'),
]
