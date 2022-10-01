from django.db import models
from django.utils import timezone
from uuid import uuid4

# Create your models here.


class College(models.Model):

    static_id = models.UUIDField(default = uuid4,editable = False,unique = True)
    name = models.CharField("Name of the college",max_length = 50)

    def __str__(self) -> str:
        return f"{self.name}"

class Category(models.Model):

    static_id = models.UUIDField(default = uuid4,editable = False,unique = True)
    name = models.CharField(max_length = 30)
    college = models.ForeignKey("College",related_name = "categories",on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"{self.college.name} - {self.name}"


class Post(models.Model):

    static_id = models.UUIDField(default = uuid4,editable = False,unique = True)
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

    def __str__(self) -> str:
        return f"{self.post}"