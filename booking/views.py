from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404
from booking.models import StockItem, Products
from django.core.urlresolvers import reverse
from django.contrib import messages


class RemoveStockItem(RedirectView):
    permanent = False
    def get_redirect_url(self, pk):
        product = get_object_or_404(Products, pk=pk)
        try:
            StockItem.objects.filter(product=product, order__isnull=True)[0].delete()
        except IndexError:
            messages.error(self.request, 'Nothing to do.')
        return reverse('product_detail', args=(pk,))

class AddStockItem(RedirectView):
    permanent = False
    def get_redirect_url(self, pk):
        product = get_object_or_404(Products, pk=pk)
        StockItem(product=product).save()
        return reverse('product_detail', args=(pk,))

