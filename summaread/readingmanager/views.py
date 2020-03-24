from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Book, Summary


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


class SummaryListView(LoginRequiredMixin, TemplateView):
    model = Summary
    template_name = "readingmanager/summary_list.html"

    def get_context_data(self, **kwargs):
        context = super(SummaryListView, self).get_context_data(**kwargs)
        context['book'] = Book.objects.filter(pk=self.kwargs['pk']).first()
        context['summary_list'] = Summary.objects.filter(
            book=self.kwargs['pk'])
        return context


class CreateSummaryView(LoginRequiredMixin, CreateView):
    model = Summary
    fields = ['title', 'Start Page', 'End Page', 'summary']
    template_name = 'readingmanager/summary_create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateSummaryView, self).get_context_data(**kwargs)
        context['book'] = Book.objects.filter(pk=self.kwargs['pk']).first()
        return context

    def form_valid(self, form):
        form.instance.book = Book.objects.filter(pk=self.kwargs['pk']).first()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('summary_list', args=[self.kwargs['pk']])


class EditSummaryView(LoginRequiredMixin, UpdateView):
    model = Summary
    pk_url_kwarg = 'summary_pk'
    fields = ['title', 'Start Page', 'End Page', 'summary']
    template_name = 'readingmanager/summary_update.html'

    def get_context_data(self, **kwargs):
        context = super(EditSummaryView, self).get_context_data(**kwargs)
        context['book'] = Book.objects.filter(
            pk=self.kwargs['book_pk']).first()
        return context

    def get_success_url(self):
        return reverse_lazy('summary_list', args=[self.kwargs['book_pk']])


class DeleteSummaryView(LoginRequiredMixin, DeleteView):
    model = Summary
    pk_url_kwarg = 'summary_pk'

    def get_context_data(self, **kwargs):
        context = super(DeleteSummaryView, self).get_context_data(**kwargs)
        context['book'] = Book.objects.filter(
            pk=self.kwargs['book_pk']).first()
        return context

    def get_success_url(self):
        return reverse_lazy('summary_list', args=[self.kwargs['book_pk']])
