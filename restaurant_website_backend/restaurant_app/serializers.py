from rest_framework import serializers
from .models import Section, Dish, Reservation

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish 
        fields = ['id', 'dish_name', 'dish_description', 'dish_price', 'dish_image', 'section']

class SectionSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True, read_only=True, source='dish_set')

    class Meta:
        model = Section 
        fields = ['id', 'section_name', 'dishes']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'guest_name', 'guest_surname', 'guest_count', 'reservation_time', 'guest_comment']