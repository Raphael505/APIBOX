from django.contrib import admin

#  registrar o modelo BOX para que ele apareça na interface de administração do Django
from .models import box

class BoxAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero')
    search_fields=('numero',)
admin.site.register(box, BoxAdmin)
