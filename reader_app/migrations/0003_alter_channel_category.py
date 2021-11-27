# Generated by Django 3.2.9 on 2021-11-27 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reader_app', '0002_auto_20211126_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channels', to='reader_app.category'),
        ),
    ]
