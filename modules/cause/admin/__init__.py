from django.contrib import admin
from modules.cause.models.cause_models import cause

@admin.register(cause)
class CauseAdmin(admin.ModelAdmin):
    
    def Cause(obj):
        return obj
    
    list_display=['name']