from django.urls import path
from knox import views as knox_views
from . import views
from django.urls import path

urlpatterns = [
    path('user/', views.get_user),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('child_add/', views.ADD_CHILD),
    path('child_mdata/', views.ADD_mDATA),
    path('child_adata/', views.ADD_aDATA),
    path('getdata/',views.get_data),
    path('children/',views.get_child),

]