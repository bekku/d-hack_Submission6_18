from django.contrib import admin
from .models import jsonres_model
class jsonres_only_Admin(admin.ModelAdmin):
    list_display = ('id', 'jsonres_nama', 'coment',
                    'age')
    list_display_links = ('id', 'jsonres_nama')

admin.site.register(jsonres_model, jsonres_only_Admin)
