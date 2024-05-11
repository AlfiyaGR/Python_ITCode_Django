from django.urls import path
from core import views


urlpatterns = [
    path('', views.index, name='home'),
    path('schools/', views.get_all_schools, name='schools'),
    path('teachers/', views.get_all_teachers, name='teachers'),
    path('groups/', views.get_all_groups, name='groups'),
    path('group/<int:group_id>', views.get_group, name='group'),
]
