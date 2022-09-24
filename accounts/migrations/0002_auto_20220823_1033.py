# Generated by Django 4.0.6 on 2022-08-23 10:33
from django.db import migrations


def create_profiles(apps, schema_editor):
    user = apps.get_model('auth', 'User')
    profile = apps.get_model('accounts', 'Profile')
    for user in user.objects.filter(profile__isnull=True):
        profile.objects.create(user=user)


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_profiles, migrations.RunPython.noop)
    ]