# Generated by Django 3.0.5 on 2020-04-22 16:47

from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True, validators=[login.models.userValidate])),
                ('password', models.CharField(max_length=32)),
                ('logged_in', models.BooleanField(default=False)),
            ],
        ),
    ]
