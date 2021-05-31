
from django.urls import path
from . import views

urlpatterns = [
    path('', views.robotics, name='robotics'),
    path('robot/<slug:robot_type>', views.robot, name='robot'),
]
