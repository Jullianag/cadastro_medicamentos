from django.contrib import admin
from . models import Remedio, Categoria


class RemedioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ean', 'marca', 'quantidade', 'principio_ativo', 'dosagem', 'descricao',
                    'data_criacao')
    list_per_page = 10
    search_fields = ('nome', 'marca', 'principio_ativo')
    list_editable = ('marca', 'dosagem', 'quantidade', 'principio_ativo')


admin.site.register(Categoria)
admin.site.register(Remedio, RemedioAdmin)
