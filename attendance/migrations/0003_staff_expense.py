# Generated by Django 4.0.5 on 2022-07-06 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_expense'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff_expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.DateField()),
                ('total_salary', models.IntegerField()),
            ],
        ),
    ]
