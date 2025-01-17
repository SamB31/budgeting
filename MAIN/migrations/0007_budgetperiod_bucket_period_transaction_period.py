# Generated by Django 4.2.13 on 2024-06-29 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0006_alter_bucket_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bucket',
            name='period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buckets', to='MAIN.budgetperiod'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='MAIN.budgetperiod'),
        ),
    ]
