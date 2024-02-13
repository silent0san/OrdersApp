from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my_order/', views.my_order, name='my-order'),
    path('group_order/', views.group_order, name='group-order'),
    path('delete_dish/<dish_id>', views.delete_dish, name='delete-dish'),

]

'''    path('group_order/', views.group_order, name='group-order'),
    path('summary', views.summary, name='summary'),'''