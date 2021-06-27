from django.contrib import admin

from .models import *

admin.site.register(Comment, admin.ModelAdmin)
admin.site.register(Talk, admin.ModelAdmin)
