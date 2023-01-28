from django.urls import path

from core.view import PromoView

app_name = 'core'

urlpatterns = [
    path('promo/', PromoView.as_view(), name='promo'),
]
