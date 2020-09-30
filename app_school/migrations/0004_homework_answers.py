# Generated by Django 3.1.1 on 2020-09-30 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_school', '0003_auto_20200930_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='homework_answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.FileField(null=True, upload_to='answers')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_school.homework')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
