from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name',unique=True, null=True, default=None)

    def save (self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            self.slug = f"{base_slug}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(models.Model):
    STATUS = {
        ('0', 'DRAFT'),
        ('1', 'PUBLISH')
    }
    SECTION = {
        ('Recent', 'Recent'),
        ('Popular', 'Popular'),
        ('Trending', 'Trending')
    }


    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    blog_slug = AutoSlugField(populate_from='title',unique=True, null=True, default=None)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length = 1, default = 0)
    section = models.CharField(max_length=200, choices=SECTION, default='Recent')
    Main_post = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title} ({self.category})"
    

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    blog_id = models.IntegerField(blank=True, null=True)
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.post:
            self.blog_id = self.post.id
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.comment}"
    


