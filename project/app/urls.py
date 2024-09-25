from django.urls import path
from app import views
urlpatterns = [
path('home/',views.home,name='home'),
path('register/',views.register,name='register'),
path('login/',views.login,name='login'),
# path('User_login/',views.User_login,name='User_login'),
# path('register_Data/',views.register_Data,name='register_Data'),
# path('logout/',views.logout,name='logout')
]