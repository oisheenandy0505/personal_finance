from django.db import models

class Entry(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    credit_debit = models.CharField(max_length=6, choices=[('Credit', 'Credit'), ('Debit', 'Debit')])
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
