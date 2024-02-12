from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from datetime import date

# Create your models here.

POSITION_CHOICES = (('BUY','BUY'), ('SELL','SELL'))
STATUS_CHOICES = (('OPEN','OPEN'), ('CLOSED','CLOSED'))
STOCK_CHOICES = (('TSLA','TSLA'),('UBER','UBER'),('AAPL','AAPL'),('AMZN','AMZN'),('AMD','AMD'),('RIOT','RIOT'),('NVDA','NVDA'),('NFLX','NFLX'),('SNAP','SNAP'),('META','META'))
# RESULT_CHOICES = (('WIN','WIN'), ('LOSS','LOSS'))
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
    trade_amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    opening_price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
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

    closing_price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', blank=True)
    date_closed = models.DateField()

    # result = models.CharField(
    #     max_length = 4,
    #     choices = RESULT_CHOICES,
    #     default = 'WIN',
    #     blank=True
    # )

    broker = models.CharField(
        max_length = 20,
        choices = BROKER_CHOICES,
        default = 'ETORO',
        blank=True
    )

    @property
    def trade_duration(self):
        trade_duration = self.date_closed.date() - self.date_opened.date()
        return trade_duration

    @property
    def units_transacted(self):
        units_transacted = self.trade_amount / self.opening_price
        return units_transacted

    @property
    def realised_pl(self):
        realised_pl = (self.units_transacted * self.closing_price) - self.trade_amount
        return realised_pl

    @property
    def result(self):
        if self.realised_pl > 0:
            return "WIN"
        elif self.realised_pl == 0:
            return "NO CHANGE"
        else:
            return "LOSS"

    class Meta:
        ordering = ["-date_opened"]

    def __str__(self):
        return f'{self.date_opened} {self.position} {self.ticker} {self.trade_amount}'
    




    

