# Generated by Django 4.1.7 on 2023-04-03 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_course_result_sem1_alter_course_result_sem2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.CharField(blank=True, default='', max_length=4),
        ),
    ]
