from django.urls import path
from .views import LoginView, RegisterView, ProfileView, LogoutView, EditProfile

app_name = 'todo_user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit-profile/', EditProfile.as_view(), name='edit_profile'),
]
