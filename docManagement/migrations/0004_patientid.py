# Generated by Django 3.0.5 on 2020-05-27 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docManagement', '0003_auto_20200524_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(default='0', max_length=10)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docManagement.Doctor')),
            ],
        ),
    ]