from django.contrib import admin

from .models import *

admin.site.register(Topic, admin.ModelAdmin)
admin.site.register(Discuss, admin.ModelAdmin)
