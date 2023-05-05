from django.db import models

# Create your models here.
class Tool(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name




# from django.db import models
# from django.contrib.auth.models import User

# class Project(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     start_date = models.DateField()
#     end_date = models.DateField()
#     STATUS_CHOICES = (
#         ('Active', 'Active'),
#         ('Close', 'Close'),
#     )
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

# class Tool(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_deleted = models.BooleanField(default=False)

#     def __str__(self):
#         return self.name

# class Skill(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_deleted = models.BooleanField(default=False)

#     def __str__(self):
#         return self.name

# class Employee(models.Model):
#     name = models.CharField(max_length=255)
#     designation = models.CharField(max_length=255)
#     professional_summary = models.TextField()
#     EMPLOYEE_STATUS_CHOICES = (
#         ('Current', 'Current'),
#         ('Ex', 'Ex'),
#     )
#     employee_status = models.CharField(max_length=10, choices=EMPLOYEE_STATUS_CHOICES)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

# class EmployeeProjectMapping(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class EmployeeCodingSkills(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class EmployeeTools(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
