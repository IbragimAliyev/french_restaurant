from django.urls import path 
from .views import SectionListView, DishListView, ReservationListView

urlpatterns = [
    path("sections/", SectionListView.as_view(), name="section-list"),
    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("reservations/", ReservationListView.as_view(), name="reservation-list"),
]
