
from django.urls import path
from .import views
app_name='filmapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('film/<int:filmid>/',views.detail,name='detail'),
    path('add/',views.addfilm,name='addfilm'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]