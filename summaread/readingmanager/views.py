from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'readingmanager/book_list.html'

    def get_queryset(self):
        queryset = Book.objects.filter(user=self.request.user)
        return queryset


class CreateBookView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'readingmanager/create_book.html'
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditBookView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'readingmanager/edit_book.html'
    success_url = reverse_lazy('book_list')

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteBookView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')

    def test_func(self):
        return self.request.user == self.get_object().user
