from django.contrib import admin

from .models import *

admin.site.register(Solution, admin.ModelAdmin)
admin.site.register(Filter, admin.ModelAdmin)