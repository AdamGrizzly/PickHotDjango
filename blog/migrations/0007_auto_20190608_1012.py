# Generated by Django 2.2.2 on 2019-06-08 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190608_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcontent',
            name='image',
            field=models.ImageField(upload_to='blog/static/img/'),
        ),
    ]
