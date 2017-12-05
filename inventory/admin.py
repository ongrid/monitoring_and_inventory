from django.contrib import admin
from inventory.models import *

class PartTypeAdmin(admin.ModelAdmin):
    list_display = ['type', 'sort']
    class Meta:
        model = PartType


class PartAdmin(admin.ModelAdmin):
    list_display = ['type', 'part','serial', 'broken', 'comment', 'last_update']
    class Meta:
        model = Part


class WorkerPartAdmin(admin.ModelAdmin):
    list_display = ['worker', 'get_parts', 'last_update']
    class Meta:
        model = WorkerPart

admin.site.register(PartType, PartTypeAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(WorkerPart, WorkerPartAdmin)