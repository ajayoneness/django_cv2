from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.opencv,name="camera" ),
    path('video/',views.video, name ="video")
]
