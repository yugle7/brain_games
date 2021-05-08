from django.contrib import admin

from .models import *

admin.site.register(Poll, admin.ModelAdmin)
admin.site.register(Choice, admin.ModelAdmin)

admin.site.register(Filter, admin.ModelAdmin)
admin.site.register(Vote, admin.ModelAdmin)
