from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('result', views.display_result, name='display_result'),
]