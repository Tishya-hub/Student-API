# Generated by Django 3.2.9 on 2021-11-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_site', '0003_marks_data_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='Name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='Roll_Number',
            field=models.IntegerField(unique=True),
        ),
    ]
