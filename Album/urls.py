from django.urls import path,include
from . import views
urlpatterns = [
    path('album/',views.AlbumCreate.as_view(),name='album'),
    path('',views.home,name='home'),
    path('editalbum/<int:id>',views.editAlbum,name='editAlbum'),
    path('deletealbum/<int:id>',views.deletealbum,name='deletealbum'),
]