# Generated by Django 4.2 on 2023-05-02 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_coursemodel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodel',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='coursemodel',
            name='type',
            field=models.CharField(choices=[('Core', 'Core'), ('Elective', 'Elective'), ('Others', 'Others')], max_length=30),
        ),
    ]