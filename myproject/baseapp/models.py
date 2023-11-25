from django.db import models


class Topic(models.Model):
    text = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Returns string value"""
        return self.text

# Create your models here.
