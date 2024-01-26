from django.db import models

class FinancialFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class FinancialDataSet(models.Model):
    financial_file = models.ForeignKey(FinancialFile, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    revenue = models.DecimalField(max_digits=12, decimal_places=4)
    expenses = models.DecimalField(max_digits=12, decimal_places=4)
    profit = models.DecimalField(max_digits=12, decimal_places=4)