from django.contrib import admin # The django.contrib includes a variety of codes, for example admin, to solve web-development problems.
from .models import MyPost

# Register your models here.

admin.site.register(MyPost)
