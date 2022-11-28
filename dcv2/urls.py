from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aj/',views.opencv,name="camera" ),
    path('',views.video, name ="video")
]
