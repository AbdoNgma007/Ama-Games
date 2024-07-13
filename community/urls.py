from django.urls import path
from . import views

urlpatterns = [
    path('', views.communities, name="communities"),
    path('<int:com_id>', views.community, name="community"),
    path('newcomment/<int:com_id>', views.createComment, name="newcomment"),
]