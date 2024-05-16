from django.urls import path
from events import views

urlpatterns = [
    path('', views.EventList.as_view(), name='Event_list'),
    path('<int:pk>/', views.EventDetail.as_view(), name='Event_detail'),
]