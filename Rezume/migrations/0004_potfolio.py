# Generated by Django 5.0 on 2023-12-20 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rezume', '0003_contact_remove_testomonial_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Potfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
