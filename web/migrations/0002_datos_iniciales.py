from django.db import migrations

SERVICIOS = [
    ("pc", "Computadoras de escritorio",
     "Diagnóstico y reparación de equipos que no encienden, se reinician o se apagan solos. "
     "Fuentes de poder, placas madre, memorias y almacenamiento."),
    ("laptop", "Notebooks y portátiles",
     "Reparación de placas, puertos de carga, bisagras, teclados y pantallas. "
     "Limpieza interna y cambio de pasta térmica."),
    ("monitor", "Monitores",
     "Monitores que no dan imagen, parpadean o tienen líneas. Reparación de fuentes, "
     "placas T-CON, retroiluminación y placas principales."),
    ("gpu", "Tarjetas gráficas",
     "Artefactos en pantalla, sin video o sobrecalentamiento. Reparación de VRM, "
     "memorias, mantenimiento y cambio de pads y pasta térmica."),
    ("chip", "Reparación a nivel componente",
     "Microsoldadura y reemplazo de chips, MOSFET, condensadores y conectores. "
     "Reparamos la placa en vez de cambiarla, ahorrándote dinero."),
    ("datos", "Diagnóstico y presupuesto",
     "Revisamos tu equipo y te explicamos la falla y el costo antes de reparar. "
     "Sin sorpresas."),
]


def crear(apps, schema_editor):
    Servicio = apps.get_model("web", "Servicio")
    DatosNegocio = apps.get_model("web", "DatosNegocio")
    for orden, (icono, nombre, descripcion) in enumerate(SERVICIOS):
        Servicio.objects.create(
            icono=icono, nombre=nombre, descripcion=descripcion, orden=orden
        )
    DatosNegocio.objects.get_or_create(
        pk=1,
        defaults={
            "telefono": "+00 000 000 000",
            "whatsapp": "",
            "email": "contacto@ejemplo.com",
            "direccion": "Calle Ejemplo 123, Ciudad",
            "horario": "Lunes a viernes 10:00 a 19:00 · Sábados 10:00 a 14:00",
        },
    )


class Migration(migrations.Migration):
    dependencies = [("web", "0001_inicial")]
    operations = [migrations.RunPython(crear, migrations.RunPython.noop)]
