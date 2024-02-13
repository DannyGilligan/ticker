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
            'trade_amount': 'Trade amount',
            'opening_price': 'Opening price',
            'position': 'Position',
            'trade_status': 'Trade status',
            'broker': 'Broker',
            'closing_price': 'Closing price',
            'date_closed': 'Date closed',
        }
        widgets = {
            'trader': forms.TextInput(attrs={'class': 'form-control'}),

            'ticker': forms.CharField(
                widget=forms.Select(choices=STOCK_CHOICES)),

            'date_opened': forms.DateField,

            'trade_amount': forms.TextInput,

            'opening_price': forms.NumberInput,

            'position': forms.CharField(
                widget=forms.Select(choices=POSITION_CHOICES)),

            'trade_status': forms.CharField(
                widget=forms.Select(choices=STATUS_CHOICES)),

            'broker': forms.CharField(
                widget=forms.Select(choices=BROKER_CHOICES)),

            'closing_price': forms.NumberInput,

            'date_closed': forms.DateField,
        }
