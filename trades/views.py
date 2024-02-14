from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Trade
from .forms import TradeDetailsForm

# Create your views here.
def index(request):
    """
    Renders the default home page
    """
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


# The add_trade_details code below was adapted from a Django crash 
# course tutorial published by YouTube channel 'Bob's Programming Academy"
# link: https://youtu.be/EUMpUUXKvP0?si=BM8WFT2mUgI9I0sI

def add_trade_details(request):
    """
    The add_trade details view will allow the user to pass
    cleaned data through the TradeDetailsForm and save the
    data, Once the new trade data is accepted, the user will
    be directed to a confirmation screen informing them
    that the trade has been updated successfully. If the
    data was invalid, the form will be rendered again to the
    user allowing them to enter valid details.
    """
    if request.method == 'POST':
        form = TradeDetailsForm(request.POST) 
        if form.is_valid():
            new_trader = form.cleaned_data['trader']
            new_ticker = form.cleaned_data['ticker']
            new_date_opened = form.cleaned_data['date_opened']
            new_trade_amount = form.cleaned_data['trade_amount']
            new_opening_price = form.cleaned_data['opening_price']
            new_position = form.cleaned_data['position']
            new_trade_status = form.cleaned_data['trade_status']
            new_broker = form.cleaned_data['broker']
            new_closing_price = form.cleaned_data['closing_price']
            new_date_closed = form.cleaned_data['date_closed']

            new_trade = Trade(
                trader = new_trader,
                ticker = new_ticker,
                date_opened = new_date_opened,
                trade_amount = new_trade_amount,
                opening_price = new_opening_price,
                position = new_position,
                trade_status = new_trade_status,
                broker = new_broker,
                closing_price = new_closing_price,
                date_closed = new_date_closed
            )
            new_trade.save()
            return render(request, 'trades/confirm_add.html')
    else:
        form = TradeDetailsForm()
    return render(request, 'trades/add_trade.html', {
        'form': TradeDetailsForm()
        })


# The edit_trade code below was adapted from a Django crash 
# course tutorial published by YouTube channel 'Bob's Programming Academy"
# link: https://youtu.be/EUMpUUXKvP0?si=BM8WFT2mUgI9I0sI


def edit_trade(request, id):
    """
    The edit_trade view will allow the user to pass
    cleaned data through the TradeDetailsForm and save the
    data, the form will be rendered with the trade data related to the
    selected trade already populated in the form fields (the trade id 
    primary key is used here to achieve this). Once the updated 
    data is accepted, the user will be directed to a confirmation
    screen informing them that the trade has been updated successfully.
    If the data was invalid, the form will be rendered again to the
    user allowing them to enter valid details.
    """
    if request.method =='POST':
        trade = Trade.objects.get(pk=id)
        form = TradeDetailsForm(request.POST, instance=trade)
        if form.is_valid():
            form = TradeDetailsForm(request.POST, instance=trade)
            form.save()
            return render(request, 'trades/confirm_edit.html')
    else:
        trade = Trade.objects.get(pk=id)
        form = TradeDetailsForm(instance=trade)
    return render(request, 'trades/edit_trade.html', {
        'form': form
        })


def delete_trade(request, id):
    """
    The delete_trade view will delete the selected
    trade from the database then redirect the user
    back to the main menu screen.
    """
    if request.method == 'POST':
        trade = Trade.objects.get(pk=id)
        trade.delete()
    return render(request, 'trades/confirm_delete.html')