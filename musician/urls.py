from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/',views.Usrlogin.as_view(),name='login'),
    path('register/',views.Register.as_view(),name='register'),
    path('logout/', views.UrsLogout, name='logout'),
    path('editmusic/<int:id>', views.editmusic, name='editmusic'),
]