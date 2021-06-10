from django.db import models

# Create your models here.
property_type = (
    ('S', 'sale'),
    ('R', 'rent')
)
class Property(models.Model):
    name = models.CharField(max_length = 50)
    property_type = models.CharField(choices = property_type, max_length=10)
    price = models.PositiveIntegerField() 
    area = models.DecimalField(decimal_places=0, max_digits=5) 
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField() 
    image = models.ImageField(upload_to='property/', null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=30)