from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2026)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",null=False) #Harry potter 1 => harry-potter-1

    #overwrite built in save method
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)



    def __str__(self):
        return f"{self.title} ({self.year})"
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name}, price:({self.price})"
