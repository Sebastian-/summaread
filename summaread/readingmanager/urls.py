from django.urls import path

from .views import BookListView, CreateBookView, EditBookView, DeleteBookView, SummaryListView, CreateSummaryView, EditSummaryView, DeleteSummaryView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('create/', CreateBookView.as_view(), name='create_book'),
    path('edit/<int:pk>', EditBookView.as_view(), name='edit_book'),
    path('delete/<int:pk>', DeleteBookView.as_view(), name='delete_book'),
    path('<int:pk>/summaries/', SummaryListView.as_view(), name='summary_list'),
    path('<int:pk>/summaries/create',
         CreateSummaryView.as_view(), name='create_summary'),
    path('<int:book_pk>/summaries/<int:summary_pk>/edit',
         EditSummaryView.as_view(), name='summary_edit'),
    path('<int:book_pk>/summaries/<int:summary_pk>/delete',
         DeleteSummaryView.as_view(), name='summary_delete'),
]
