# Generated by Django 4.0.5 on 2022-08-06 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anti_d_app', '0003_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='disaster_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anti_d_app.disastername'),
        ),
        migrations.AlterField(
            model_name='report',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='作成日時'),
        ),
    ]
