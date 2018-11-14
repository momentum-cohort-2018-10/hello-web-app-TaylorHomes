from django.contrib import admin

from collection.models import Villians


class VillainAdmin(admin.ModelAdmin):
    model = Villians
    list_display = (
        'name',
        'description',
    )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Villians, VillainAdmin)

# Register your models here.
