from django.contrib import admin
from .models import Otziv
# Register your models here.


@admin.register(Otziv)
class OtzivAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ['name', 'email', 'address']


