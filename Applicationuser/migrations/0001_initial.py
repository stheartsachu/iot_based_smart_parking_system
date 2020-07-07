# Generated by Django 2.0.6 on 2020-03-09 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application_user',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=False)),
                ('email', models.CharField(default='', max_length=200, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('phone_no', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=250)),
                ('otp', models.CharField(max_length=200, null=True)),
                ('otp_gen_time', models.CharField(max_length=200, null=True)),
                ('user_type', models.CharField(max_length=200, null=True)),
                ('token', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
