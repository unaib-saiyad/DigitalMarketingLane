from django.db import models


# Create your models here.

class Invoice(models.Model):
    invoice_number = models.IntegerField(primary_key=True, blank=False, null=False)
    customer_name = models.CharField(max_length=200, blank=False, null=False)
    date = models.DateField(blank=False, null=False)

    def __str__(self):
        return f"{self.invoice_number}"


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    unit_price = models.FloatField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False)

    def __str__(self):
        return f"{self.invoice}"
