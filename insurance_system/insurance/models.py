from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name
class InsurancePolicy(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    policy_name = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=50)
    premium_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.policy_name        