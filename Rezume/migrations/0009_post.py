# Generated by Django 5.0 on 2023-12-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rezume', '0008_alter_education_start_at_alter_resume_start_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]