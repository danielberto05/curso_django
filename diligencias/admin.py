from django.contrib import admin

from diligencias.models import Diligencia

class DiligenciaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_realizacao', 'dinheiro_apreendido']
    search_fields = ['nome']

admin.site.register(Diligencia, DiligenciaAdmin)
