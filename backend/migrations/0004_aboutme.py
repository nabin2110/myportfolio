# Generated by Django 5.0 on 2024-02-13 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
