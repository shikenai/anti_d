# Generated by Django 4.0.5 on 2022-08-06 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anti_d_app', '0005_report_hearing_at_report_related_organization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='related_organization',
        ),
        migrations.AddField(
            model_name='report',
            name='related_organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anti_d_app.relatedorganization'),
        ),
    ]
