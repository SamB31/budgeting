# Generated by Django 4.2.13 on 2024-06-29 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0007_budgetperiod_bucket_period_transaction_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bucket',
            name='period',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='period',
        ),
        migrations.DeleteModel(
            name='BudgetPeriod',
        ),
    ]