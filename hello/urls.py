from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.index, name= 'first'),
    path('introduction/', views.introduction, name='intro'),
    path('About/', views.About, name='us')
]
