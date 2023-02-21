from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(College)
# admin.site.register(Post)
admin.site.register(Category)
# admin.site.register(PostImage)
admin.site.register(Book)
admin.site.register(Video)
admin.site.register(Misc)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','category')
    list_filter = ('category','category__college')

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post','category','college','caption')
    list_filter = ('post','post__category','post__category__college')

    def category(self,obj):
        return obj.post.category

    def college(self,obj):
        return obj.post.category.college    


