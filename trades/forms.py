from django import forms
from .models import Trade

class TradeDetailsForm(forms.ModelForm):
    class Meta:
        model = Trade
        formFields = ['trader', 'ticker', 'date_opened', 'trade_amount', 'opening_price', 'position', 'units_transacted', 'trade_status', 'broker', 'closing_price', 'date_closed', 'trade_duration', 'realised_pl', 'result']
        formLabels = {
            'trader': 'Trader',
            'ticker': 'Ticker',
            'date_opened': 'Date opened',
            'trade_amount': 'Trade amount',
            'opening_price': 'Opening price',
            'position': 'Position',
            'trade_status': 'Trade status',
            'broker': 'Broker',
            'closing_price': 'Closing price',
            'date_closed': 'Date closed'
        }
        widgets = {
            'trader': forms.TextInput(attrs={'class': 'form-control'}),

            'ticker': forms.Charfield(
                widget=forms.Select(choices=STOCK_CHOICES),
                attrs={'class': 'form-control'}), 

            'date_opened': forms.DateField(attrs={'class': 'form-control'}),

            'trade_amount': forms.TextInput(attrs={'class': 'form-control'}),

            'opening_price': forms.NumberInput(attrs={'class': 'form-control'}),

            'position': forms.Charfield(
                widget=forms.Select(choices=POSITION_CHOICES),
                attrs={'class': 'form-control'}),

            'trade_status': forms.Charfield(
                widget=forms.Select(choices=STATUS_CHOICES),
                attrs={'class': 'form-control'}),

            'broker': forms.Charfield(
                widget=forms.Select(choices=BROKER_CHOICES),
                attrs={'class': 'form-control'}),

            'closing_price': forms.NumberInput(attrs={'class': 'form-control'}),

            'date_closed': forms.DateField(attrs={'class': 'form-control'}),
        }
