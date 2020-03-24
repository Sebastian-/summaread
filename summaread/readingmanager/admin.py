from django.contrib import admin

from .models import Book, Summary


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "user",)


class SummaryAdmin(admin.ModelAdmin):
    list_display = ("book", "title", "Start Page", "End Page")


admin.site.register(Book, BookAdmin)
admin.site.register(Summary, SummaryAdmin)
