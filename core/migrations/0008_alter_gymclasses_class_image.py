# Generated by Django 4.2.7 on 2023-12-23 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_gymclasses_class_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymclasses',
            name='class_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
