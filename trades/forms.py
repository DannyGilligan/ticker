from django import forms
from .models import Trade

POSITION_CHOICES = (('BUY','BUY'), ('SELL','SELL'))
STATUS_CHOICES = (('OPEN','OPEN'), ('CLOSED','CLOSED'))
STOCK_CHOICES = (('TSLA','TSLA'),('UBER','UBER'),('AAPL','AAPL'),('AMZN','AMZN'),('AMD','AMD'),('RIOT','RIOT'),('NVDA','NVDA'),('NFLX','NFLX'),('SNAP','SNAP'),('META','META'))
BROKER_CHOICES = (('ETORO','ETORO'), ('ROBINHOOD','ROBINHOOD'), ('IG','IG'), ('DEGIRO','DEGIRO'), ('INTERACTIVE BROKERS','INTERACTIVE BROKERS'), ('PLUS500','PLUS500'))

class TradeDetailsForm(forms.ModelForm):
    class Meta:
        model = Trade

        fields = ['trader', 'ticker', 'date_opened', 'trade_amount', 'opening_price', 'position', 'trade_status', 'broker', 'closing_price', 'date_closed']

        labels = {
            'trader': 'Trader',
            'ticker': 'Ticker',
            'date_opened': 'Date opened',
            'trade_amount': 'Trade amount $',
            'opening_price': 'Opening price $',
            'position': 'Position',
            'trade_status': 'Trade status',
            'broker': 'Broker',
            'closing_price': 'Closing price $',
            'date_closed': 'Date closed',
        }

        widgets = {
            'trader': forms.Select(attrs={'class': 'form-control'}),
            'ticker': forms.Select(attrs={'class': 'form-control'}),
            'date_opened': forms.DateInput(attrs={'class': 'form-control','placeholder':'Only YYYY/MM/DD format accepted'}),
            'trade_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'opening_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'trade_status': forms.Select(attrs={'class': 'form-control'}),
            'broker': forms.Select(attrs={'class': 'form-control'}),
            'closing_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_closed': forms.DateInput(attrs={'class': 'form-control','placeholder':'Only YYYY/MM/DD format accepted'}),

        }
        

