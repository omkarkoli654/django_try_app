from django.urls import path
from project_app_1 import views

app_name = 'project_app_1'

urlpatterns = [
 path ('register/',views.register,name="register"),
 path('user_login/', views.user_login,name = 'user_login'),
]
