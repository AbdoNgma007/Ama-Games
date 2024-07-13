from django.urls import path
from .import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('update', views.updateProfile, name="updateprofile"),
    path('logout', views.logout_view, name="logout"),
    path('signin', views.sign_in, name="signin"),
    path('signup', views.sign_up, name="signup"),
    path('register', views.register_view, name="reg"),
]