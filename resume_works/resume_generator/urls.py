from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    # path('projects/', views.project_list, name='project_list'),
    # path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    # path('employees/', views.employee_list, name='employee_list'),
    # path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('coding_skills/', views.skills_list, name='skills_list'),
    path('coding_skills/add_skill/', views.add_skill, name = 'add_skill'),
    # path('tools/', views.tool_list, name='tool_list'),
    # path('generate-resume/<int:pk>/', views.generate_resume, name='generate_resume'),

]