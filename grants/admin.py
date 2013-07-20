from django.contrib import admin
from grants import models


class GrantAdmin(admin.ModelAdmin):
    list_display = ['target_organization', 'budget_approved',
                    'budget_transferred', 'effective_budget', 'year', 'type',
                    'regulation', 'ministry', 'related_number']
    list_filter = ['year', 'type', 'ministry', 'regulation']
    search_fields = ['target_organization__name', 'regulation__name']


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'homepage']

admin.site.register(models.Organization, OrganizationAdmin)
admin.site.register(models.Grant, GrantAdmin)
admin.site.register(models.GrantType)
admin.site.register(models.Regulation)
admin.site.register(models.Ministry)
