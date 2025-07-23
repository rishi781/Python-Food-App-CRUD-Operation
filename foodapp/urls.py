from django.urls import path
from . import views

app_name = 'foodapp'
urlpatterns = [
    path('', views.home, name='home'),
    path("<int:id>/", views.details, name= 'details'),
    path('additem/', views.additem, name= 'additem'),
    path('update/<int:id>/',views.update_item,name='update'),
    path('delete/<int:id>/',views.delete_item,name='delete'),    
]