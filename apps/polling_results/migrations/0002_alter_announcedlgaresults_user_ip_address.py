# Generated by Django 4.2.2 on 2023-06-13 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling_results', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcedlgaresults',
            name='user_ip_address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
