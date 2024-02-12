# from . import views as trades_views
# from django.urls import path

# urlpatterns = [
#     path("", trades_views.another_test_view, name="test"),
#     path("trades", trades_views.test_view, name="trades"),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_trades/', views.all_trades, name='all_trades'),
    path('open_trades/', views.all_trades, name='open_trades'),
]