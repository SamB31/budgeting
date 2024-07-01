from django.db import models

class Income(models.Model):
    planned_income = models.DecimalField(max_digits=10, decimal_places=2)
    actual_income = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f"Planned: {self.planned_income}, Actual: {self.actual_income}"

class Bucket(models.Model):
    name = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=25)  # For storing color codes, e.g., #RRGGBB

    def __str__(self):
        return self.name

class Transaction(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    simple_description = models.CharField(max_length=100, blank=True)
    bucket = models.ForeignKey(Bucket, on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return f"{self.description} - {self.amount}"
    
    
class Saving(models.Model):
    name = models.CharField(max_length=100)
    cashamount = models.DecimalField(max_digits=10, decimal_places=2)
    cardamount = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def total(self):
        return self.cashamount + self.cardamount

    def __str__(self):
        return self.name
