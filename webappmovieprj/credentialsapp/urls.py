from django.urls import path

from . import views

app_name='credentialsapp'
urlpatterns = [

    path('registrations/',views.registrations,name='registrations'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/<int:id>/',views.updateProfile,name='update'),
]