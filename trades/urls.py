from django.urls import path
from . import views

urlpatterns = [
    path('add_trade/', views.add_trade_details, name='add_trade'),
    path('all_trades/', views.all_trades, name='all_trades'),
    path('closed_trades/', views.closed_trades, name='closed_trades'),
    path('edit_trade/<int:id>/', views.edit_trade, name='edit_trade'),
    path('open_trades/', views.open_trades, name='open_trades'),
    path('<int:id>', views.view_trade, name='view_trade'),
    path('', views.index, name='index'),
]