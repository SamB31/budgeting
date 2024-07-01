from django.contrib import admin
from .models import Income, Bucket, Transaction, Saving

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('planned_income', 'actual_income')
    

@admin.register(Bucket)
class BucketAdmin(admin.ModelAdmin):
    list_display = ('name', 'budget', 'color')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'amount', 'simple_description', 'bucket')

@admin.register(Saving)  
class SavingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'cashamount', 'cardamount', 'total')
