from django.db import models

# Create your models here.

class Comment(models.Model):
    full_name = models.CharField(max_length=500)
    company_name = models.CharField(max_length=500, null=True)
    email_address = models.EmailField(null=True)
    phone_number = models.CharField(max_length=20, null=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name


class Testimonial(models.Model):
    full_name = models.CharField(max_length=500)
    position = models.CharField(max_length=500)
    content = models.TextField()
    image = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Save your object. After this line, value of custom_id will be 0 which is default value
        self.id = 0
        super(Post, self).save(*args, **kwargs)
