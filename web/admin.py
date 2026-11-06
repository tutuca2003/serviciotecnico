from django.contrib import admin

from .models import DatosNegocio, MensajeContacto, Servicio

admin.site.site_header = "Administración de la página"
admin.site.site_title = "Administración"
admin.site.index_title = "Contenido de la página"


@admin.register(DatosNegocio)
class DatosNegocioAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not DatosNegocio.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ["nombre", "icono", "orden", "activo"]
    list_editable = ["orden", "activo"]


@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ["fecha", "nombre", "telefono", "equipo", "atendido"]
    list_filter = ["atendido"]
    list_editable = ["atendido"]
    search_fields = ["nombre", "telefono", "email", "equipo", "problema"]
    readonly_fields = ["fecha"]
