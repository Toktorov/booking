from django.db import models
from decimal import Decimal
from payments import PurchasedItem
from payments.models import BasePayment

# Create your models here.
class Payment(BasePayment):

    def get_failure_url(self):
        return 'http://example.com/failure/'

    def get_success_url(self):
        return 'hotel_index'

    def get_purchased_items(self):
        # you'll probably want to retrieve these from an associated order
        yield PurchasedItem(name='The Hound of the Baskervilles', sku='BSKV',
                            quantity=9, price=Decimal(10), currency='USD')

    class Meta:
        verbose_name = 'Переводы'
        verbose_name_plural = 'Переводы'
        ordering = ('-id',)