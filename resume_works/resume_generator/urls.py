from django.urls import path
from .views.dashboard_view import *
from .views.coding_skills_view import *
from .views.tools_view import *
from .views.projects_view import *
from .views.designations_view import *
from .views.users_view import *
from .views.employees_view import *

urlpatterns = [
    path('', home_view, name = 'home'),
    path('dashboard/', dashboard_view, name = 'dashboard'),

    #coding_skill
    path('coding_skills/', coding_skills_list_view, name='coding_skills_list'),
    path('coding_skills/create_coding_skill/', create_coding_skill_view, name = 'create_coding_skill'),
    path('coding_skills/edit_coding_skill/<int:coding_skill_id>/', edit_coding_skill_view, name = 'edit_coding_skill'),
    path('coding_skills/delete_coding_skill/<int:coding_skill_id>/', delete_coding_skill_view, name = 'delete_coding_skill'),

    #tool
    path('tools/', tools_list_view, name='tools_list'),
    path('tools/create_tool/', create_tool_view, name = 'create_tool'),
    path('tools/edit_tool/<int:tool_id>/', edit_tool_view, name = 'edit_tool'),
    path('tools/delete_tool/<int:tool_id>/', delete_tool_view, name = 'delete_tool'),

    #designations
    path('designations/', designations_list_view, name='designations_list'),
    path('designations/create_designation/', create_designation_view, name = 'create_designation'),
    path('designations/edit_designation/<int:designation_id>/', edit_designation_view, name = 'edit_designation'),
    path('designations/delete_designation/<int:designation_id>/', delete_designation_view, name = 'delete_designation'),

    #project
    path('projects/', projects_list_view, name='projects_list'),
    path('projects/create_project/', create_project_view, name = 'create_project'),
    path('projects/edit_project/<int:project_id>/', edit_project_view, name = 'edit_project'),
    path('projects/delete_project/<int:project_id>/', delete_project_view, name = 'delete_project'),

    #user-HR
    path('users/', users_list_view, name = 'users_list'),

    #employee
    path('employees/', employees_list_view, name='employees_list'),
    path('employees/create_employee/', create_employee_view, name = 'create_employee'),
    path('employees/edit_employee/<int:employee_id>/', edit_employee_view, name = 'edit_employee'),
    path('employees/delete_employee/<int:employee_id>/', delete_employee_view, name = 'delete_employee'),

    #mapping
    path('employees/map_to_projects/', map_employee_to_projects_view, name = 'map_to_projects'),
    path('employees/map_to_projects/<int:employee_id>/', map_employee_to_projects_view, name = 'map_to_projects'),

    #resume
    path('employees/view_resume/<int:employee_id>/', employee_resume_view, name = 'view_employee_resume'),






    
    # path('generate-resume/<int:pk>/', views.generate_resume, name='generate_resume'),

]