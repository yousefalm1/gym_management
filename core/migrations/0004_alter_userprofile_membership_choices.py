# Generated by Django 4.2.7 on 2023-12-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_userprofile_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='membership_choices',
            field=models.CharField(choices=[('bronze', 'Bronze'), ('silver', 'Silver'), ('gold', 'Gold')], max_length=100),
        ),
    ]
