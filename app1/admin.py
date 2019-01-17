from django.contrib import admin
from .models import Despesa

# Register your models here.

class DespesaAdm(admin.ModelAdmin):
    list_display = ('data_criacao','tipo_despesa','descricao','forma_pag','vencimento','quitado')
    list_filter = ('vencimento','quitado')

admin.site.register(Despesa, DespesaAdm)

admin.site.site_reader='Painel de Controle'
admin.site.index_title='Recursos'
admin.site.site_title='Despesas'
