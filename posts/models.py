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
    title = models.CharField(max_length = 40)
    text = models.TextField()
    uploaded_on = models.DateTimeField(default = timezone.now)
    category = models.ForeignKey("Post",related_name = 'posts',on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.title

class PostImage(models.Model):

    post = models.ForeignKey('Post',related_name = 'images',on_delete = models.CASCADE)
    photo = models.ImageField()

    def __str__(self) -> str:
        return self.post