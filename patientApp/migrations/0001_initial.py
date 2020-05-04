# Generated by Django 3.0.6 on 2020-05-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('age', models.IntegerField()),
                ('aadharNumber', models.IntegerField()),
                ('bloodGrp', models.CharField(max_length=10)),
                ('address', models.TextField(blank=True)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('disease', models.CharField(max_length=15)),
                ('createdDate', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modifiedDate', models.DateTimeField(auto_now=True, verbose_name='Modified')),
            ],
        ),
    ]
