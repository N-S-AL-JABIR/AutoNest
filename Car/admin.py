from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ["brand_name", "model_name", "quantity"]
    list_filter = ["quantity"]

    def brand_name(self, obj):
        return obj.brand.name


admin.site.register(Car, CarAdmin)
