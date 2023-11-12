from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('register/',views.register_page, name="register"),
    path('profile/',views.profile, name="profile"),
    path('password_change/', views.custom_password_change_view.as_view(), name='password_change'),
    path('user-home/', views.user_home, name="user_home"),
]
