from django.contrib import admin

from .models import *

admin.site.register(Category, admin.ModelAdmin)
admin.site.register(Puzzle, admin.ModelAdmin)
