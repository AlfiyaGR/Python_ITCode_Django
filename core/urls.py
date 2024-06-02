from django.template.defaulttags import url
from django.urls import path
from core import views

urlpatterns = [
    # главная страница (вход учителя и ученика)
    path('', views.home, name='home'),
    path('home_stud/', views.home_stud, name='home_stud'),
    path('home_admin/', views.home_admin, name='home_admin'),

    path('get_student', views.get_student, name='get_student'),
    path('get_teacher', views.get_teacher, name='get_teacher'),
    path('get_admin', views.get_admin, name='get_admin'),

    # списки
    path('schools/', views.SchoolList.as_view(), name='schools'),

    # личный кабинет учителя
    path('teacher/<int:pk>/', views.TeacherDetail.as_view(), name='teacher'),
    path('schedule/<int:pk>/', views.ScheduleList.as_view(), name='schedule'),
    path('school/<int:pk>/', views.SchoolDetail.as_view(), name='school'),
    path('group/<int:pk>/', views.GroupDetail.as_view(), name='group'),
    path('marks/<int:pk>/', views.MarkDetail.as_view(), name='marks'),
    path('lessons/<int:pk>/', views.LessonDetail.as_view(), name='lessons'),
    path('homeworks/<int:pk>/', views.HomeworkList.as_view(), name='homeworks'),

    path('teacher/lesson/<int:pk>/post/', views.post_lesson, name='post_lesson'),

    # личный кабинет ученика
    path('student/<int:pk>/', views.StudentDetail.as_view(), name='student'),
    path('stud_schedule/<int:pk>/', views.StudScheduleList.as_view(), name='stud_schedule'),
    path('stud_group/<int:pk>/', views.StudGroupDetail.as_view(), name='stud_group'),
    path('stud_school/<int:pk>/', views.StudSchoolDetail.as_view(), name='stud_school'),
    path('stud_marks/<int:pk>/', views.StudMarkDetail.as_view(), name='stud_marks'),
    path('stud_lessons/<int:pk>/<int:lesson_pk>', views.StudLessonDetail.as_view(), name='stud_lessons'),
    path('stud_homeworks/<int:pk>/<int:lesson_pk>', views.StudHomeworkDetail.as_view(), name='stud_homeworks'),

    # личный кабинет администратора
    path('administrator/<int:pk>/', views.AdminDetail.as_view(), name='administrator'),
    path('teachers/<int:pk>', views.TeacherList.as_view(), name='teachers'),
    path('groups/<int:pk>', views.GroupList.as_view(), name='groups'),
    path('admin_school/<int:pk>/', views.AdminSchoolDetail.as_view(), name='admin_school'),
    path('subjects/<int:pk>', views.SubjectList.as_view(), name='subjects'),
    path('schedules/<int:pk>', views.AllScheduleList.as_view(), name='schedules'),

    path('teacher/<int:pk>/post/', views.post_teacher, name='post_teacher'),
    path('teacher/<int:pk>/<int:pk_teacher>/edit/', views.edit_teacher, name='edit_teacher'),
    path('teacher/<int:pk>/<int:pk_teacher>/delete/', views.delete_teacher, name='delete_teacher'),

    path('school/<int:pk>/<int:pk_school>/edit/', views.edit_school, name='edit_school'),

    path('subject/<int:pk>/post/', views.post_subject, name='post_subject'),
    path('subject/<int:pk>/<int:pk_subject>/edit/', views.edit_subject, name='edit_subject'),
    path('subject/<int:pk>/<int:pk_subject>/delete/', views.delete_subject, name='delete_subject'),

    path('admin_panel/<int:pk>/edit/', views.edit_admin, name='edit_admin'),

    path('lesson/<int:pk>/post/', views.post_lesson_admin, name='admin_post_lesson'),
    path('lesson/<int:pk>/<int:pk_lesson>/edit/', views.edit_lesson_admin, name='admin_edit_lesson'),
    path('lesson/<int:pk>/<int:pk_lesson>/delete/', views.delete_lesson, name='admin_delete_lesson'),

    # все остальное
    path('redirect/', views.RedirectAdmin.as_view(), name='redirect'),
]
