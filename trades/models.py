from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Trade(models.Model):
    trader = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ticker_trade"
    )
    ticker = models.CharField(max_length=5)
    

