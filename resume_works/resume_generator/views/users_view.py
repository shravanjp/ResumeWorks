from django.contrib.auth.models import User
from django.shortcuts import render

def users_list_view(request):
    users = User.objects.all()
    logged_in_user = request.user

    return render(request, 'resume_generator/user/users_list.html', {'users': users,'logged_in_user': logged_in_user,})

