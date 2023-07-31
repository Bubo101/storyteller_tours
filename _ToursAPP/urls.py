from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.tour_list, name='tour-list'),
    path('tours/<int:pk>/', views.tour_detail, name='tour-detail'),
    path('stops/', views.stop_list, name='stop-list'),
    path('stops/<int:pk>/', views.stop_detail, name='stop-detail'),
    path('substops/', views.substop_list, name='substop-list'),
    path('substops/<int:pk>/', views.substop_detail, name='substop-detail'),
]
