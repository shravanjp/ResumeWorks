# Generated by Django 4.2 on 2023-05-09 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_generator', '0004_designation_project_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='coding_skills_used',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tools_used',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
