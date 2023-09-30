from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
import json
from django.views.generic import ListView , DetailView ,TemplateView
# from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Category, Product
from .forms import ReviewForm
 
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context 


class AboutView(TemplateView):
    template_name = "about.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context 

class ContactView(TemplateView):
    template_name = 'contact.html'
    form_class = ReviewForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()	
        context["form"] = self.form_class()
        return context 
   
    def post(self, request,  *args, **kwargs ):
        form = self.form_class(request.POST)
		
        if form.is_valid():
            form.save()
        return redirect('contact')

class CatDetailView(DetailView):
    model = Category
    template_name = 'product_details.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context 


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["cat"] = Category.objects.filter(id=self.object.categpry.id)
        context["category"] = Category.objects.all()
        
        return context 
