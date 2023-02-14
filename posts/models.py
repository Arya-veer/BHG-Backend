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
    description = models.TextField(blank=True)
    col_img = models.ImageField(upload_to=college_image_path,null=True)
    col_img2 = models.ImageField(upload_to=college_image_path_2,null=True)


    def __str__(self) -> str:
        return f"{self.name}" 

def category_image_path(instance,filename):
    return f"{instance.college.name}/{instance.name}/banner.{filename.split('.')[-1]}"
class Category(models.Model):

    static_id = models.UUIDField(default = uuid4,editable = True,unique = True)
    name = models.CharField(max_length = 30)
    college = models.ForeignKey("College",related_name = "categories",on_delete = models.CASCADE)
    categ_img = models.ImageField(upload_to=category_image_path,null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"{self.college.name} - {self.name}"


class Post(models.Model):

    static_id = models.UUIDField(default = uuid4,editable = True,unique = True)
    title = models.CharField(max_length = 40,blank = True)
    text = models.TextField(blank = True)
    uploaded_on = models.DateTimeField(default = timezone.now)
    category = models.ForeignKey("Category",related_name = 'posts',on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.title

def post_image_path(instance,filename):
    return f"{instance.post.category.college.name}/{instance.post.category.name}/{instance.post.title}/{filename}"
class PostImage(models.Model):

    """
    One post can have multiple images
    """

    post = models.ForeignKey('Post',related_name = 'images',on_delete = models.CASCADE)
    photo = models.ImageField(upload_to = post_image_path)
    caption = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return f"{self.post}"