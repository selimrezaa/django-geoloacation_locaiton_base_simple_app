from django.urls import path
from first_app import views


urlpatterns = [
    path('', views.index, name="index"),
    path('locator/', views.locator, name='locator'),
    path('get-user-ip/', views.get_user_ip, name='get_user_ip'),
    # path('location/', views.location, name='location'),


    path('user-form/', views.user_form, name='user_form'),
]
