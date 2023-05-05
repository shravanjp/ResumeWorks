from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    # path('projects/', views.project_list, name='project_list'),
    # path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    # path('employees/', views.employee_list, name='employee_list'),
    # path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('coding_skills/', views.coding_skills_list, name='skills_list'),
    # path('coding_skills/create_skill/', views.create_skill, name = 'create_skill'),
    # path('coding_skills/edit_skill/', views.create_skill, name = 'create_skill'),

    # path('tools/', views.tool_list, name='tool_list'),
    # path('generate-resume/<int:pk>/', views.generate_resume, name='generate_resume'),

]