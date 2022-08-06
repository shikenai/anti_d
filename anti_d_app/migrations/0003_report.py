# Generated by Django 4.0.5 on 2022-08-05 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anti_d_app', '0002_disastername_alter_localgovernment_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_title', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(verbose_name='作成日時')),
            ],
        ),
    ]