from django.db import models

class CodingSkill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Tool(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    tools_used = models.ManyToManyField(Tool, related_name='projects')
    coding_skills_used = models.ManyToManyField(CodingSkill, related_name='projects')
    roles_responsibility = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    PROJECT_STATUS_CHOICES = (
        ('active', 'Active'),
        ('close', 'Closed'),
    )
    status = models.CharField(max_length=10, choices=PROJECT_STATUS_CHOICES,default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project)
    professional_summary = models.TextField()
    coding_skills = models.ManyToManyField(CodingSkill)
    tools = models.ManyToManyField(Tool)
    EMPLOYEE_STATUS_CHOICES = (
        ('current', 'Current'),
        ('ex', 'Ex'),
    )
    employment_status = models.CharField(max_length=10, choices=EMPLOYEE_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# class EmployeeProjectMapping(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

