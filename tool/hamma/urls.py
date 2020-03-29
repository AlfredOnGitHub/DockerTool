from django.urls import path
from hamma import views

app_name = 'hamma'

urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('user_login/',views.user_login,name='user_login'),
    path('app/', views.app, name='app'),
]