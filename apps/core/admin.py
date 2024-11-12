from django.contrib import admin
from apps.core import models

admin.site.register(models.Client)
admin.site.register(models.RegisterLocation)

# admin.site.register(models.Immobile)
# admin.site.register(models.ImmobileImages)

class ImmobileImagesInlineAdmin(admin.TabularInline):
    model = models.ImmobileImages
    extra = 0

class ImmobileAdmin(admin.ModelAdmin):
    inlines = [ImmobileImagesInlineAdmin]

admin.site.register(models.Immobile, ImmobileAdmin)
