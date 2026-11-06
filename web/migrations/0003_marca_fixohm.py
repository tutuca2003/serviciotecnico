from django.db import migrations, models

NOMBRE_VIEJO = "Servicio Técnico"
ESLOGAN_VIEJO = "Reparación de computadoras, monitores y tarjetas gráficas a nivel componente"
NOMBRE = "FixOhm"
ESLOGAN = "No cambiamos la placa: la reparamos. Recuperamos lo que otros dan por perdido."


def poner_marca(apps, schema_editor):
    # Solo cambia los textos que siguen con el valor de fábrica,
    # así no pisa lo que ya hayas escrito desde el panel.
    DatosNegocio = apps.get_model("web", "DatosNegocio")
    DatosNegocio.objects.filter(nombre=NOMBRE_VIEJO).update(nombre=NOMBRE)
    DatosNegocio.objects.filter(eslogan=ESLOGAN_VIEJO).update(eslogan=ESLOGAN)


class Migration(migrations.Migration):
    dependencies = [("web", "0002_datos_iniciales")]
    operations = [
        migrations.AlterField(
            model_name="datosnegocio",
            name="nombre",
            field=models.CharField(default=NOMBRE, max_length=100),
        ),
        migrations.AlterField(
            model_name="datosnegocio",
            name="eslogan",
            field=models.CharField(default=ESLOGAN, max_length=200),
        ),
        migrations.RunPython(poner_marca, migrations.RunPython.noop),
    ]
