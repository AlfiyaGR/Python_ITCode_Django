from django.template.defaulttags import url
from django.urls import path
from core import views


urlpatterns = [
    # главная страница (вход учителя и ученика)
    path('', views.home, name='home'),
    path('home_stud/', views.home_stud, name='home_stud'),
    path('get_student', views.get_student, name='get_student'),
    path('get_teacher', views.get_teacher, name='get_teacher'),

    # списки
    path('schools/', views.SchoolList.as_view(), name='schools'),
    path('teachers/', views.TeacherList.as_view(), name='teachers'),
    path('groups/', views.GroupList.as_view(), name='groups'),

    # личный кабинет учителя
    path('teacher/<int:pk>/', views.TeacherDetail.as_view(), name='teacher'),
    path('schedule/<int:pk>/', views.ScheduleList.as_view(), name='schedule'),
    path('school/<int:pk>/', views.SchoolDetail.as_view(), name='school'),
    path('group/<int:pk>/', views.GroupDetail.as_view(), name='group'),

    # личный кабинет ученика
    path('student/<int:pk>/', views.StudentDetail.as_view(), name='student'),
    path('stud_schedule/<int:pk>/', views.StudScheduleList.as_view(), name='stud_schedule'),
    path('stud_group/<int:pk>/', views.StudGroupDetail.as_view(), name='stud_group'),
    path('stud_school/<int:pk>/', views.StudSchoolDetail.as_view(), name='stud_school'),

    # все остальное
    path('lessons/<int:pk>/', views.LessonDetail.as_view(), name='lessons'),
    path('homeworks/<int:pk>/', views.HomeworkList.as_view(), name='homeworks'),

    path('redirect/', views.RedirectAdmin.as_view(), name='redirect'),
]