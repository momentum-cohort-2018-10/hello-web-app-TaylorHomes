from django.contrib import admin

from collection.models import Villians


class VillainsAdmin(admin.ModelAdmin):
    model = Villians
    list_display = (
        'name',
        'description',
    )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Villians, VillainsAdmin)

# Register your models here.
