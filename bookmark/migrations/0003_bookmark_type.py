# Generated by Django 4.0.7 on 2022-09-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_bookmark_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='TYPE'),
        ),
    ]
