from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ProductModel


class ProductListView(ListView):
    model = ProductModel
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'product_detail.html'


class ProductCreateView(CreateView):
    model = ProductModel
    template_name = 'product_form.html'
    fields = ['name', 'price', 'description', 'seller', 'color', 'product_dimensions']
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = ProductModel
    template_name = 'product_form.html'
    fields = ['name', 'price', 'description', 'seller', 'color', 'product_dimensions']
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = ProductModel
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')