from django.conf.urls import patterns, url
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from booking.models import ProductsCategory, Products

urlpatterns = patterns('',
        url(r'^categories/$', user_passes_test(lambda u: u.is_admin)(ListView.as_view(model=ProductsCategory)), name='booking_category_list'),
        url(r'^categories/add/$', user_passes_test(lambda u: u.is_admin)(CreateView.as_view(model=ProductsCategory)), name='productscategory_new'),
        url(r'^categories/edit/(?P<pk>\d+)/$', user_passes_test(lambda u: u.is_admin)(UpdateView.as_view(model=ProductsCategory)), name='productscategory_update'),
        url(r'^categories/(?P<pk>\d+)/$', user_passes_test(lambda u: u.is_admin)(DetailView.as_view(model=ProductsCategory)), name='productscategory_detail'),
        url(r'^products/$', user_passes_test(lambda u: u.is_admin)(ListView.as_view(model=Products)), name='product_list'),
        url(r'^products/add/$', user_passes_test(lambda u: u.is_admin)(CreateView.as_view(model=Products)), name='product_new'),
        url(r'^products/edit/(?P<pk>\d+)/$', user_passes_test(lambda u: u.is_admin)(UpdateView.as_view(model=Products)), name='product_update'),
        url(r'^products/(?P<pk>\d+)/$', user_passes_test(lambda u: u.is_admin)(DetailView.as_view(model=Products)), name='product_detail'),
    )

