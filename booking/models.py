from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

class ProductsCategory(models.Model):
    class meta:
        verbose_name=_('products category')
        verbose_name_plural=_('products categories')
        ordering = ['order']

    name = models.CharField(_('name'),max_length=64)
    ordering = models.IntegerField(_('order'), help_text=_('0 will be on top'))

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('productscategory_detail', args=[str(self.id)])

class Products(models.Model):
    class meta:
        verbose_name=_('product')
        verbose_name_plural=_('products')
        ordering = ['order']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    name = models.CharField(_('name'),max_length=128)
    ordering = models.IntegerField(_('order'), help_text=_('0 will be on top'))
    category = models.ForeignKey(ProductsCategory)

class StockItem(models.Model):
    class meta:
        verbose_name=_('stock item')
        verbose_name_plural=_('stock items')

    product = models.ForeignKey(Products)
    order = models.ForeignKey('Order', null=True)

class Order(models.Model):
    class meta:
        verbose_name=_('Order')
        verbose_name_plural=_('Orders')

    donation = models.IntegerField(_('donation'), blank=True, help_text=_('A non-mandatory donation to the LSM 2013 organisation team'))
    invoice = models.BooleanField('invoice', help_text=_('Do you need an invoice?'))
    external_comment = models.IntegerField('comment', blank=True)
    internal_comment = models.IntegerField('internal comment', blank=True, help_text=_('available only to the admins'))
    paid = models.BooleanField('paid', default=False)
    order_date = models.DateTimeField(_('creation date'), null=True)
    payment_date = models.DateField('payment date', null=True)
    payment_type = models.CharField('payment type', max_length=64, null=True)

