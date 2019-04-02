from django.urls import path
from . import views
from . import views2

app_name = 'usuario'
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/<int:pk>', views.Profile.as_view(), name='profile'),
    path('password_change/', views.ChangePassword.as_view(),
         name='change_password'),
]
