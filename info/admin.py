from django.contrib import admin

from .models import Contact
from .models import Project

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'contact_date')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'email', 'contact_date')
    list_per_page = 20
admin.site.register(Contact, ContactAdmin)




class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Project, ProjectAdmin)