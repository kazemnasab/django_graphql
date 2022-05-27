from django.contrib import admin
from .schema.category import Category
from .schema.book import Book
from .schema.grocery import Grocery

# Register your models here.

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Grocery)