from django.contrib import admin
from .models import Blog, BlogComment, TopBlogPage
# Register your models here.

admin.site.register(TopBlogPage)

class BlogAdmin(admin.ModelAdmin):
    list_display =('title', 'author_name', 'created_date','modified_date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)


class BlogCommentAdmin(admin.ModelAdmin):
    list_display =('blog','name', 'phone', 'email', 'created_date')

admin.site.register(BlogComment, BlogCommentAdmin)

