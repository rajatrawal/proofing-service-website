# Generated by Django 4.2.2 on 2023-06-14 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_carousel_service_alter_image_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='home.category'),
        ),
    ]
