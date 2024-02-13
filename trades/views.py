from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Trade
from .forms import TradeDetailsForm

# Create your views here.
def index(request):
    return render(request, 'trades/index.html')


def all_trades(request):
    """
    The 'trades' variable below holds all the data in the
    'Trade' model, this is the context that allows
    the all_trades.html template to display the
    requested information to the user when rendered.
    """
    return render(request, 'trades/all_trades.html', {
        'trades': Trade.objects.all()
    })


def open_trades(request):
    """
    The 'open_trades' variable below holds all the data in the
    'Trade' model filtered by 'OPEN' status, this is the context that allows
    the open_trades.html template to display the
    requested information to the user when rendered.
    """
    return render(request, 'trades/open_trades.html', {
        'open_trades': Trade.objects.filter(trade_status="OPEN")
    })


def closed_trades(request):
    """
    The 'closed_trades' below variable holds all the data in the
    'Trade' model filtered by 'CLOSED' status, this is the context that allows
    the closed_trades.html template to display the
    requested information to the user when rendered.
    """
    return render(request, 'trades/closed_trades.html', {
        'closed_trades': Trade.objects.filter(trade_status="CLOSED")
    })


def view_trade(request, id):
    trade = Trade.objects.get(pk=id)
    return HttpeResponseDirect(reverse('index'))

