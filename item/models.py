# import a built-in User models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        # order by name
        ordering = ('name',)
        # rename model
        verbose_name_plural = 'Categories'

    # show the name of the column for model
    def __str__(self):
        return self.name


class Item(models.Model):
    # set a foreign key
    category = models.ForeignKey(
        Category, related_name='items', on_delete=models.CASCADE)
    # add char field column
    name = models.CharField(max_length=255)
    # add text/String field column
    description = models.TextField(blank=True, null=True)
    # add float/double field column
    price = models.FloatField()
    # add an image field column, to upload images
    # can only be used with 'pillow' library == 'pip install pillow'
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    # add boolean field column
    is_sold = models.BooleanField(default=False)
    createdBy = models.ForeignKey(
        User, related_name="items", on_delete=models.CASCADE)
    # add date field column, "auto_now_add" == get current date/time
    created_at = models.DateTimeField(auto_now_add=True)

    # show the name of the column for model
    def __str__(self):
        return self.name
