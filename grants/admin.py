from django.contrib import admin
from grants import models

admin.site.register(models.Organization)
admin.site.register(models.Grant)
admin.site.register(models.Regulation)
admin.site.register(models.Ministry)
