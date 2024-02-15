from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from datetime import date
from djmoney.money import Money
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator



# Create your models here.

POSITION_CHOICES = (('BUY','BUY'), ('SELL','SELL'))
STATUS_CHOICES = (('OPEN','OPEN'), ('CLOSED','CLOSED'))
STOCK_CHOICES = (('TSLA','TSLA'),('UBER','UBER'),('AAPL','AAPL'),('AMZN','AMZN'),('AMD','AMD'),('RIOT','RIOT'),('NVDA','NVDA'),('NFLX','NFLX'),('SNAP','SNAP'),('META','META'))
BROKER_CHOICES = (('ETORO','ETORO'), ('ROBINHOOD','ROBINHOOD'), ('IG','IG'), ('DEGIRO','DEGIRO'), ('INTERACTIVE BROKERS','INTERACTIVE BROKERS'), ('PLUS500','PLUS500'))

class Trade(models.Model):

    trader = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ticker_trade"
    )

    ticker = models.CharField(
        max_length=5,
        choices = STOCK_CHOICES
    )

    date_opened = models.DateField()
    
    trade_amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', validators=[MinMoneyValidator(1),])
    
    opening_price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', validators=[MinMoneyValidator(1),])
    
    position = models.CharField(
        max_length = 4,
        choices = POSITION_CHOICES,
        default = 'BUY'
    )

    trade_status = models.CharField(
        max_length = 6,
        choices = STATUS_CHOICES,
        default = 'OPEN'
    )

    broker = models.CharField(
        max_length = 20,
        choices = BROKER_CHOICES
    )

    closing_price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', blank=True, null=True, validators=[MinMoneyValidator(1),])

    date_closed = models.DateField(blank=True, null=True)

    @property
    def trade_duration(self):
        if self.date_closed == None:
            return "PENDING"
        else:
            trade_duration = self.date_closed - self.date_opened
            return trade_duration

    @property
    def units_transacted(self):
        units_transacted = self.trade_amount / self.opening_price
        return round(units_transacted, 2)

    @property
    def realised_pl(self):
        if self.closing_price == None:
            return "PENDING"
        else:
            realised_pl = (self.units_transacted * self.closing_price) - self.trade_amount
            return realised_pl

    @property
    def result(self):
        realised_pl_string = str(self.realised_pl)
        zero_amount_string = str(0.00)
        if realised_pl_string == "PENDING":
            return "PENDING"
        elif realised_pl_string > zero_amount_string:
            return "WIN"
        elif realised_pl_string == zero_amount_string:
            return "NO CHANGE"
        else:
            return "LOSS"

    class Meta:
        ordering = ["date_opened"]
    

    def __str__(self):
        return f'{self.date_opened} {self.position} {self.ticker} {self.trade_amount}'
    




    

