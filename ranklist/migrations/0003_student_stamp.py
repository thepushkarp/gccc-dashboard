# Generated by Django 3.1.1 on 2020-10-11 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranklist', '0002_student_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
