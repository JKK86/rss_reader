# Generated by Django 3.2.9 on 2021-11-26 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reader_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channels', to='reader_app.category'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='copyright',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='channel',
            name='last_build_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='reader_app.channel'),
        ),
    ]
