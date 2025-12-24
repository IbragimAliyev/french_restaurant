from django.db import models

# Create your models here.
class Section(models.Model):
    section_name = models.CharField(max_length=25)

    def __str__(self):
        return self.section_name

class Dish(models.Model):
    dish_name = models.CharField(max_length=25)
    dish_description = models.CharField(max_length=255)
    dish_price = models.CharField(max_length=25)
    dish_image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.dish_name 
    
class Reservation(models.Model):
    guest_name = models.CharField(max_length=25)
    guest_surname = models.CharField(max_length=25)
    guest_count = models.IntegerField()
    reservation_time = models.TimeField()
    guest_comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.guest_name