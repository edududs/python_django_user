from django.contrib import admin


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tel', 'email')
    list_display_links = ('id', 'nome', 'email')
    # list_filter = ('nome', 'sobrenome')
    list_per_page = 15
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_editable = ('tel')