from django.contrib import admin

from blog.models import BlogPost, BlogPostTag

admin.site.register(BlogPostTag)

class TagInline(admin.TabularInline):
    model = BlogPost.tags.through
    verbose_name = 'Blog Post Tag'
    verbose_name_plural = 'Blog Post Tags'
    extra = 0

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    inlines = [
        TagInline
    ]
    exclude = (
        'tags',
    )