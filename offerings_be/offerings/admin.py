from django.contrib import admin
from .models import Offerings


class OfferingsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Offerings, OfferingsAdmin)

