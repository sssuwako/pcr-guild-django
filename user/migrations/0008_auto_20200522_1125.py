# Generated by Django 3.0.6 on 2020-05-22 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guild', '0005_auto_20200522_1125'),
        ('user', '0007_auto_20200521_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='operate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='operaters', to='guild.Guild'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='d9d1ad649bdb11eab41ed46d6df5224b', max_length=36, primary_key=True, serialize=False),
        ),
    ]
