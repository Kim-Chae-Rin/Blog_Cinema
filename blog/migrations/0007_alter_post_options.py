# Generated by Django 4.0.7 on 2022-09-30 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('modify_dt',), 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
    ]