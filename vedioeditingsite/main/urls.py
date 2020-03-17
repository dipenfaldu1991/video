from . import views
from django.urls import path


urlpatterns = [
    path('',views.index,name='index'),
    path('upload/', views.showvideo, name='upload'),
    path('trim/', views.trim_view, name='trim'),
    path('looping/', views.looping_view, name='looping'),
    path('download/',views.download,name='download'),
    path('clip_mirror_x/', views.clip_mirror_x, name='clip_mirror_x'),
    path('clip_mirror_y/', views.clip_mirror_y, name='clip_mirror_y'),
    path('clip_rotate/', views.clip_rotate, name='clip_rotate'),
    path('clip_freeze/', views.clip_freeze, name='clip_freeze'),
    path('clip_invertcolour/', views.clip_invertcolour, name='clip_invertcolour'),
    path('clip_blackandwhite/', views.clip_blackandwhite, name='clip_blackandwhite'),
]