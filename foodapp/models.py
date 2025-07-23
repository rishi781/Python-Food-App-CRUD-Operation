from django.db import models

# Create your models here.
class FoodMenu(models.Model):
    item_name = models.CharField(max_length=255)  
    description = models.CharField(max_length=122)
    price = models.DecimalField(max_digits=7, decimal_places=2)  
    image_url = models.URLField(max_length=500)

    def __str__(self):
      return f"{self.id} - {self.item_name} - {self.price}"  # for displaying id in database
