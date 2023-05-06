from django.urls import path
from .views.dashboard_view import *
from .views.coding_skills_view import *
from .views.tools_view import *

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

    #project
    # path('projects/', views.projects_list, name='projects_list'),
    # path('projects/create_tool/', views.create_project, name = 'create_project'),
    # path('projects/edit_project/<int:project_id>/', views.edit_project, name = 'edit_project'),
    # path('projects/delete_project/<int:project_id>/', views.delete_project, name = 'delete_project'),

    
    # path('generate-resume/<int:pk>/', views.generate_resume, name='generate_resume'),

]