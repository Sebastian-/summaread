from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'readingmanager/book_list.html'

    def get_queryset(self):
        queryset = Book.objects.filter(user=self.request.user)
        return queryset
