from django.db import models

class Phone(models.Model):
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.model

class Purchase(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=100)
    buyer_phone = models.CharField(max_length=15)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.buyer_name} - {self.phone.model}"
