# Generated by Django 4.1.1 on 2022-09-24 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(blank=True, verbose_name='date of creation')),
                ('name', models.CharField(max_length=50, verbose_name='album name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='album description')),
                ('user', models.ManyToManyField(related_name='albums', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', verbose_name='image')),
                ('description', models.TextField(verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date of creation')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='webapp.album', verbose_name='photos')),
                ('user', models.ManyToManyField(related_name='photos', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'photos',
                'verbose_name_plural': 'Photos',
                'db_table': 'photos',
            },
        ),
    ]
