# Generated by Django 4.2.7 on 2023-12-29 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_gymclasses_instructors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='membership_choices',
            field=models.CharField(choices=[('bronze', 'Bronze'), ('silver', 'Silver'), ('gold', 'Gold'), ('none', 'None')]),
        ),
    ]
