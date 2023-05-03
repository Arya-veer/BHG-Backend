from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(FrontPage)
admin.site.register(Footer)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','college')
    list_filter = ('college',)
    search_fields = ('title','text')

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post','college','caption')
    list_filter = ('post','post__college')
    search_fields = ('post__title','post__text','caption')

    def college(self,obj):
        return obj.post.college 

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title','college')
    list_filter = ('college',)
    search_fields = ('title',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author')
    search_fields = ('title','author','description')

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name',)
       
