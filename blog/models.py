from django.db import models


# Create your models here.

class Blog(models.Model):
    """ Model for the blog post """
    title = models.CharField(max_length=200)
   
    blog_post = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text