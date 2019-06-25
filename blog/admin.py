from django.contrib import admin
from blog.models import Blog, BlogAuthor, BlogComment

# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogAuthor)
admin.site.register(BlogComment)

# Define the admin class
# class BlogAuthorAdmin(admin.ModelAdmin):
#     pass

# # Register the admin class with the associated model
# admin.site.register(BlogAuthor, AuthorAdmin)


# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     pass

# # Register the Admin classes for BookInstance using the decorator
# @admin.register(BookInstance) 
# class BlogCommentAdmin(admin.ModelAdmin):
#     pass