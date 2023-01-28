from django.shortcuts import render
from django.views import View

from core.forms import ContactForm
from core.models import SliderItem


class PromoView(View):
    def get(self, request, *args, **kwargs):
        slider_items = SliderItem.objects.all()
        contact_form = ContactForm()
        return render(request, 'core/promo.html', {'slider_items': slider_items, 'contact_form': contact_form})
