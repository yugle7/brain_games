from django.contrib import admin

from .models import *

admin.site.register(Tag, admin.ModelAdmin)

admin.site.register(Activity, admin.ModelAdmin)
