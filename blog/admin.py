from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
  list_display = ("title", "author", "date_posted")
  readonly_fields = ('date_posted', 'last_update')
  search_fields = ("title", "author", "date_posted")
  date_hierarchy = "date_posted"

admin.site.register(Post, PostAdmin)
