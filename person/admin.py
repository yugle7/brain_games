from django.contrib import admin

from .models import *

admin.site.register(Role, admin.ModelAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'rating', 'money')
    search_fields = ('username',)
    list_editable = ('role',)
    list_filter = ('rating', 'money')


admin.site.register(Person, PersonAdmin)

admin.site.register(Filter, admin.ModelAdmin)

