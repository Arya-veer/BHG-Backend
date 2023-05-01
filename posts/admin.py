from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(College)
admin.site.register(Book)
admin.site.register(Video)
admin.site.register(FrontPage)
admin.site.register(Footer)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','college')
    list_filter = ('college',)

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post','college','caption')
    list_filter = ('post','post__college')


    def college(self,obj):
        return obj.post.college    


