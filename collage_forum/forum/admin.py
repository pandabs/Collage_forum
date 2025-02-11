from django.contrib import admin
from .models import Forum

class ForumAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'description')

admin.site.register(Forum, ForumAdmin)