# Generated by Django 5.0 on 2023-12-21 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rezume', '0004_potfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
    ]
