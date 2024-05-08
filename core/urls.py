from django.urls import path
from core import views


urlpatterns = [
    path('', views.index),
    path('schools/', views.index, name='schools'),
    path('teachers/', views.get_teachers, name='teachers'),
    path('groups/', views.get_groups, name='groups')
]
