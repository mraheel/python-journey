from django.urls import path
from events import views

urlpatterns = [
    path('events/', views.EventList.as_view(), name='Event_list'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='Event_detail'),
    path('category/', views.CategoryViewSet.as_view(), name='Category'),
]