from django.shortcuts import render
from django.views.generic import View
from .models import *

# Create your views here
class BaseView(View):
    views = {}
    views['categories'] = Category.objects.all()

class HomeView(BaseView):
    def get(self,request):
        self.views
        self.views['ads'] = Ad.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['galleries'] = Gallery.objects.all()
        self.views['services'] = Service.objects.all()
        self.views['all_products'] = Product.objects.filter(labels = 'all')
        self.views['new_products'] = Product.objects.filter(labels = 'new')
        self.views['featured_products'] = Product.objects.filter(labels = 'featured')
        self.views['offer_products'] = Product.objects.filter(labels = 'offer')

        return render(request, 'index.html', self.views)
