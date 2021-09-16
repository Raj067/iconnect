# Generated by Django 3.2.5 on 2021-09-16 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=500)),
                ('company_name', models.CharField(max_length=500, null=True)),
                ('email_address', models.EmailField(max_length=254, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]