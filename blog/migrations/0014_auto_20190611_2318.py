# Generated by Django 2.2.2 on 2019-06-11 17:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0013_guests_hotdeals'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HotDeals',
            new_name='Hot',
        ),
    ]
