# Generated by Django 4.0.3 on 2022-03-28 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
