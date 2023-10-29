# Generated by Django 4.0.3 on 2023-06-30 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_delete_newsletter_alter_social_icon_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('twitter_link', models.CharField(max_length=200)),
                ('facebook_link', models.CharField(max_length=200)),
                ('instagram_link', models.CharField(max_length=200)),
                ('linkedin_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ContactNowText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HeadDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('video_link', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
                ('map_link', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ServicesText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]
