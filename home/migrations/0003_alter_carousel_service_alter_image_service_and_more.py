# Generated by Django 4.2.2 on 2023-06-14 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_carousel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousels', to='home.service'),
        ),
        migrations.AlterField(
            model_name='image',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.service'),
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='home.category'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_request', to='home.service'),
        ),
    ]
