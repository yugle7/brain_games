from django.contrib import admin

from .models import *

admin.site.register(Discuss, admin.ModelAdmin)
admin.site.register(Topic, admin.ModelAdmin)

admin.site.register(Filter, admin.ModelAdmin)

admin.site.register(Comment, admin.ModelAdmin)
admin.site.register(Reaction, admin.ModelAdmin)