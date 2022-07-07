from django.contrib import admin
from .models import *
from django.apps import apps
from import_export.admin import *
from import_export import resources
from django.contrib.admin.sites import AlreadyRegistered
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class RaiseTicketAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user','img','subject','msg','priority','category','subcategory','Type',
    'raised_by','status','created','updated','ticket_id','assign_to',
    'assigned_date','is_active','is_superuser','time_period')

admin.site.register(RaiseTicket,RaiseTicketAdmin)

class AutomationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('subject','msg','assign_to',
    'time_period','is_active')

admin.site.register(Automation,AutomationAdmin)


class DynamicDataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user','prefix_txn','is_active')

admin.site.register(DynamicData,DynamicDataAdmin)

class CommentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user','ticket','message','is_active')

admin.site.register(Comment,CommentAdmin)