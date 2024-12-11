from django.db import models

# Create your models here.

class Blogpost(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    Published_Date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title