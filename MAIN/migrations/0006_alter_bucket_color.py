# Generated by Django 4.2.13 on 2024-06-29 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0005_alter_transaction_bucket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucket',
            name='color',
            field=models.CharField(max_length=25),
        ),
    ]
