from django.contrib.auth.models import User
from django.shortcuts import render

def users_list_view(request):
    users = User.objects.all()
    return render(request, 'resume_generator/user/users_list.html', {'users': users})

