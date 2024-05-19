from django.urls import path
from core import views


urlpatterns = [
    path('', views.AuthorizationForm.as_view(), name='home'),
    path('schools/', views.SchoolList.as_view(), name='schools'),
    path('teachers/', views.TeacherList.as_view(), name='teachers'),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view(), name='teacher'),
    path('groups/', views.GroupList.as_view(), name='groups'),
    path('group/<int:pk>/', views.GroupDetail.as_view(), name='group'),
    path('schedule/<int:pk>/', views.ScheduleList.as_view(), name='schedule'),
    path('school/<int:pk>/', views.SchoolDetail.as_view(), name='school'),
    path('lessons/<int:pk>/', views.LessonDetail.as_view(), name='lessons'),
    path('homeworks/<int:pk>/', views.HomeworkList.as_view(), name='homeworks'),

    path('redirect/', views.RedirectAdmin.as_view(), name='redirect'),
]
