from django.contrib import admin
from . import models

admin.site.register(models.Fabonacci)


# class FabonacciAdmin(admin.ModelAdmin):
#     """Customize the look of the auto-generated admin for the Member model"""


# admin.site.register(Fabonacci, FabonacciAdmin)
