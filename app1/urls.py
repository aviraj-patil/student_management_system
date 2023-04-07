from . import views
from django.urls import path


urlpatterns = [
    path('',views.home ,name='home'),
    path('ad/', views.admission ,name='admission'),
    path('signupuser/', views.signupuser ,name='signupuser'),
    path('loginuser/', views.loginuser ,name='loginuser'),
    path('logoutuser/', views.logoutuser ,name='logoutuser'),
    path('student_table_approved/', views.student_table_approved ,name='student_table_approved'),
    path('student_table_unapproved/', views.student_table_unapproved ,name='student_table_unapproved'),
    path('cr/', views.create_result ,name='create_result'),
    path('sr/', views.all_students_results ,name='all_students_results'),
    path('<int:student_pk>', views.edit_student_info ,name='edit_student_info'),
    path('<int:student_pk>/delete', views.delete_student ,name='delete_student'),
    path('<int:student_pk>/result', views.edit_course_results ,name='edit_course_results'),
    # path('sr/',views.student_results, name='student_results')
]
