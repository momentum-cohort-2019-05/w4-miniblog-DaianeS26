from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BlogAuthor(models.Model):
    """Model representing the blogger"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=300)

    class Meta:
        ordering = ["user", "bio"]

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('authors', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.user.username


class Blog(models.Model):
    """ Model for the blog post """
    title = models.CharField(max_length=200)
    author= models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
    blog_post = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title', 'post_date']

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('blog', args=[str(self.id)])

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    """ Model representing blog comments"""
   
    comment = models.TextField(max_length=600)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        ordering = ['post_date']


    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('blog-comment', args=[str(self.id)])

    def __str__(self):

        if len(self.comment) > 50:
            return self.comment[:50] + "..."
        else:
            return self.comment
