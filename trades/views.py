from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Trade

# Create your views here.
def index(request):
    return render(request, 'trades/index.html')

def all_trades(request):
    return render(request, 'trades/all_trades.html', {
        # 'trades' variable holds all the data in the
        # Trade model, this is the context that allows
        # the all_trades.html template to display the
        # requested information to the user when rendered.
        'trades': Trade.objects.all()
    })

def open_trades(request):
    return render(request, 'trades/open_trades.html', {
        # 'trades' variable holds all the data in the
        # Trade model, this is the context that allows
        # the all_trades.html template to display the
        # requested information to the user when rendered.
        'open_trades': Trade.objects.filter(trade_status="OPEN")
    })

def closed_trades(request):
    return render(request, 'trades/closed_trades.html', {
        # 'trades' variable holds all the data in the
        # Trade model, this is the context that allows
        # the all_trades.html template to display the
        # requested information to the user when rendered.
        'closed_trades': Trade.objects.filter(trade_status="CLOSED")
    })

