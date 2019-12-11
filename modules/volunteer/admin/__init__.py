from django.contrib import admin
from modules.volunteer.models.volunteer_models import volunteerRegistration,volunterSkills
# Register your models here.
@admin.register(volunterSkills)
class volunteerSkillsAdmin(admin.ModelAdmin):
    def skills(obj):
        return obj

    list_display=['skills',]




@admin.register(volunteerRegistration)
class volunteer_registration_admin(admin.ModelAdmin):

    def name(obj):
        return obj
    
    list_display=[name,'email','contact_no','address','skills']
    search_fields=['address',]
