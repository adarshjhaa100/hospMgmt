# Generated by Django 3.0.6 on 2020-05-07 05:12

from django.db import migrations, models
import docManagement.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='defDoc', max_length=200)),
                ('age', models.IntegerField(default=20, validators=[docManagement.models.agevalidate])),
                ('phone', models.CharField(default='1111111111', max_length=12, validators=[docManagement.models.phonevalidate])),
                ('licenseNo', models.CharField(default='1111111111', max_length=12, validators=[docManagement.models.phonevalidate])),
                ('address', models.TextField(blank=True)),
                ('speciality', models.CharField(default='physician', max_length=100)),
                ('certificate', models.FileField(upload_to='docCeritficates/', verbose_name='Certificate Add')),
            ],
        ),
    ]