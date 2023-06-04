from django.contrib import admin
from django.utils.html import format_html
from blog.models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'category', 'images', 'author')
    list_filter = ['title']

    def images(self, obj):
        return format_html(f'''<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')


admin.site.register(Category)
