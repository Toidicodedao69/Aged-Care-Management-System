# Generated by Django 5.0.3 on 2024-05-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_service_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(choices=[('Individual', 'Individual'), ('Group', 'Group')], max_length=50),
        ),
    ]
