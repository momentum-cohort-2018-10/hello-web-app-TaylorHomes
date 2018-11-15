from django.contrib import admin

from collection.models import Villain


class VillainAdmin(admin.ModelAdmin):
    model = Villain
    list_display = (
        'name',
        'description',
    )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Villain, VillainAdmin)
