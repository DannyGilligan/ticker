# Generated by Django 4.2.10 on 2024-02-14 09:20

from django.db import migrations
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0005_alter_trade_broker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='closing_price',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default_currency='USD', max_digits=10, null=True, validators=[djmoney.models.validators.MinMoneyValidator(10)]),
        ),
        migrations.AlterField(
            model_name='trade',
            name='opening_price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=10, validators=[djmoney.models.validators.MinMoneyValidator(10)]),
        ),
        migrations.AlterField(
            model_name='trade',
            name='trade_amount',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=10, validators=[djmoney.models.validators.MinMoneyValidator(10)]),
        ),
    ]
