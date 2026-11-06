from django.db import models


class DatosNegocio(models.Model):
    """Datos de contacto que aparecen en toda la página. Solo existe uno."""

    nombre = models.CharField(max_length=100, default="FixOhm")
    eslogan = models.CharField(
        max_length=200,
        default="No cambiamos la placa: la reparamos. Recuperamos lo que otros dan por perdido.",
    )
    telefono = models.CharField(max_length=30, blank=True)
    whatsapp = models.CharField(
        max_length=20,
        blank=True,
        help_text="Solo números con código de país, sin + ni espacios. Ej: 5215512345678",
    )
    email = models.EmailField(blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    horario = models.CharField(max_length=200, blank=True)
    mapa_url = models.URLField(
        blank=True, help_text="Enlace de Google Maps a tu local (opcional)"
    )

    class Meta:
        verbose_name = "datos del negocio"
        verbose_name_plural = "datos del negocio"

    def __str__(self):
        return self.nombre

    @classmethod
    def obtener(cls):
        datos, _ = cls.objects.get_or_create(pk=1)
        return datos


class Servicio(models.Model):
    ICONOS = [
        ("pc", "Computadora"),
        ("laptop", "Portátil"),
        ("monitor", "Monitor"),
        ("gpu", "Tarjeta gráfica"),
        ("chip", "Componente / placa"),
        ("datos", "Datos / disco"),
        ("herramienta", "Herramienta"),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    icono = models.CharField(max_length=20, choices=ICONOS, default="herramienta")
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden", "nombre"]

    def __str__(self):
        return self.nombre


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField("teléfono", max_length=30)
    email = models.EmailField(blank=True)
    equipo = models.CharField("equipo", max_length=100, help_text="Ej: Monitor LG 27\", RTX 3060")
    problema = models.TextField("descripción del problema")
    fecha = models.DateTimeField(auto_now_add=True)
    atendido = models.BooleanField(default=False)

    class Meta:
        ordering = ["-fecha"]
        verbose_name = "mensaje de contacto"
        verbose_name_plural = "mensajes de contacto"

    def __str__(self):
        return f"{self.nombre} - {self.equipo}"
