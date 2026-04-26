from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ProductModel


class ProductListView(ListView):
    model = ProductModel
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProtectedListView(LoginRequiredMixin, ListView):
    model = ProductModel
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return ProductModel.objects.filter(user=self.request.user)



class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'product_detail.html'


class ProductCreateView(CreateView):
    model = ProductModel
    template_name = 'product_form.html'
    fields = ['name', 'price', 'description', 'seller', 'color', 'product_dimensions']
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = ProductModel
    template_name = 'product_form.html'
    fields = ['name', 'price', 'description', 'seller', 'color', 'product_dimensions']
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = ProductModel
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')