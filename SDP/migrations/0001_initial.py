# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 06:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(choices=[('MandA', 'Mergers and Acquisitions'), ('M', 'Markets'), ('RM', 'Risk Management'), ('S', 'Securities'), ('FM', 'Financial Modelling'), ('O', 'Operations'), ('IT', 'Information Technology')], default='MandA', max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('file', 'File'), ('image', 'Image'), ('text', 'Text')], default='text', max_length=127)),
                ('text_content', models.TextField(default='')),
                ('image_content', models.ImageField(null=True, upload_to='uploads')),
                ('file_content', models.FileField(null=True, upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=127)),
                ('description', models.TextField(max_length=2000)),
                ('open', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SDP.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('enrollment_id', models.AutoField(primary_key=True, serialize=False)),
                ('completed', models.BooleanField(default=False)),
                ('completed_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('module_id', models.AutoField(primary_key=True, serialize=False)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_title', models.CharField(choices=[('A', 'Admin'), ('I', 'Instructor'), ('H', 'HR'), ('P', 'Participant')], default='Participant', max_length=127)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SDP.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='component',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SDP.Course'),
        ),
    ]
