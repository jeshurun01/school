from django.urls import path

from . import views


app_name = 'profiles'
urlpatterns = [
    path('register/', views.sign_up, name='register'),
    path('profile/', views.profile_page, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit'),
]
