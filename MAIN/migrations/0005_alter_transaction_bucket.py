# Generated by Django 4.2.13 on 2024-06-29 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0004_rename_savings_saving'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='bucket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MAIN.bucket'),
        ),
    ]
