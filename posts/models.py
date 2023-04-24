from django.db import models
from django.utils import timezone
from uuid import uuid4

# Create your models here.
def college_image_path(instance,filename):
    return f"{instance.name}/banner.{filename.split('.')[-1]}"

def college_image_path_2(instance,filename):
    return f"{instance.name}/banner_2.{filename.split('.')[-1]}"

class College(models.Model):

    static_id = models.UUIDField(default = uuid4,unique = True)
    name = models.CharField("Name of the college",max_length = 50)
    title = models.CharField("Title of the college",max_length = 50,blank=True)


    def __str__(self) -> str:
        return f"{self.name}" 

def category_image_path(instance,filename):
    return f"{instance.college.name}/{instance.title}/banner.{filename.split('.')[-1]}"

class Post(models.Model):

    static_id = models.UUIDField(default = uuid4,editable = True,unique = True)
    title = models.CharField(max_length = 40,blank = True)
    text = models.TextField(blank = True)
    uploaded_on = models.DateTimeField(default = timezone.now)
    college = models.ForeignKey("College",related_name = 'posts',on_delete = models.CASCADE)
    image = models.ImageField(upload_to = category_image_path,null=True)

    def __str__(self) -> str:
        return self.title

def post_image_path(instance,filename):
    return f"{instance.post.college.name}/{instance.post.title}/{instance.post.title}/{filename}"


class PostImage(models.Model):
    """ One post can have multiple images """
    post = models.ForeignKey('Post',related_name = 'images',on_delete = models.CASCADE)
    photo = models.ImageField(upload_to = post_image_path)
    caption = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return f"{self.post}"

def book_path(instance,filename):
    return f"books/{instance.title}/{filename}"

def book_cover(instance,filename):
    return f"books/{instance.title}/{filename}"

class Book(models.Model):

    static_id = models.UUIDField(default = uuid4,editable = True,unique = True)
    title = models.CharField(max_length = 40,blank = True)
    description = models.TextField(blank=True,null=True)
    bookFile = models.FileField(upload_to=book_path)
    author = models.TextField(null=True,blank=True)
    book_cover = models.ImageField(upload_to=book_cover,null=True)

    def __str__(self):
        return self.title

class Video(models.Model):

    static_id = models.UUIDField(default = uuid4,editable = True,unique = True)
    title = models.CharField(max_length = 40,blank = True)
    link = models.URLField(max_length = 200)

    def __str__(self) -> str:
        return self.title


def cover_image(instance,filename):
    return f"cover_image/{filename}"


class FrontPage(models.Model):

    cover_title = models.TextField(null=True,blank=True)
    cover_subheading = models.TextField(null=True,blank=True)
    gallery_content = models.TextField(null=True,blank=True)
    cover_desc = models.TextField(null=True,blank=True)
    cover_image = models.ImageField(upload_to=cover_image,null=True)
    about = models.TextField(null=True,blank=True)
    gallery_image = models.ImageField(upload_to=cover_image,null=True)


    def __str__(self) -> str:
        return "Front Page" + self.cover_title
    
class Footer(models.Model):

    footer_title = models.TextField(null=True,blank=True)
    footer_description = models.TextField(null=True,blank=True)
    footer_copyright = models.TextField(null=True,blank=True)
    footer_email = models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return "Footer" + self.footer_title