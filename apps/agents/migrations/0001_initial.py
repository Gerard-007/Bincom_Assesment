# Generated by Django 4.2.2 on 2023-06-12 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('polling_units', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentName',
            fields=[
                ('name_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('user_ip_address', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('polling_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polling_units.pollingunit')),
            ],
        ),
    ]
