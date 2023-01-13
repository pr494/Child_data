from django.contrib import admin
from .models import child,manual,auto
# Register your models here.
@admin.register(child)
class DataAdmin(admin.ModelAdmin):
    pass
@admin.register(manual)
class DataAdmin(admin.ModelAdmin):
    pass
@admin.register(auto)
class DataAdmin(admin.ModelAdmin):
    pass
