from django.contrib import admin
from .models import Section, Dish, Reservation
# Register your models here.

class DishInline(admin.TabularInline):  
    model = Dish
    extra = 1  

class SectionAdmin(admin.ModelAdmin):
    inlines = [DishInline]

admin.site.register(Section, SectionAdmin)
admin.site.register(Dish)
admin.site.register(Reservation)