# Generated by Django 4.2.7 on 2023-12-24 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_instructorprofile_instructor_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymclasses',
            name='instructors',
            field=models.ManyToManyField(to='core.instructorprofile'),
        ),
    ]
