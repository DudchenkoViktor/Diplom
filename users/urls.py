from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('',  views.TeacherProfileView.as_view(), name='profile'),
    path('change_form',  views.TeacherProfileUpdateView.as_view(), name='change_profile'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.UserRegestrationView.as_view(), name='registration'),
]
