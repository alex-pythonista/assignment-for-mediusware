from typing import Any
from django.db.models.query import QuerySet
from django.views import generic

from product.models import (
    Variant, ProductVariantPrice)


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class ProductVariantPriceListView(generic.ListView):
    model = ProductVariantPrice
    template_name = 'products/list2.html'
    context_object_name = 'product_variant_prices'
    paginate_by = 2
    
    def get_queryset(self):
        return ProductVariantPrice.objects.all().order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_variant_prices = ProductVariantPrice.objects.select_related('product').all().order_by('product_id', 'created_at')
        context['grouped_product_variant_prices'] = product_variant_prices
        return context