# Generated by Django 5.0.3 on 2024-03-20 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=300, null=True),
        ),
    ]
