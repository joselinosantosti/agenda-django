from django.contrib import admin
from .models import Departamento, Empregado

class EmpregadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'aniversario', 'departamento', 'foto', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome')
    list_editable = ('telefone', 'mostrar')

admin.site.register(Departamento)
admin.site.register(Empregado, EmpregadoAdmin)