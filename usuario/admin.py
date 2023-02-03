from django.contrib import admin


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'tel', 'last_name')
    list_display_links = ('id', 'first_name', 'email')
    list_editable = ('tel', 'first_name')
    list_per_page = 15
    search_fields = ('nome', 'sobrenome')
