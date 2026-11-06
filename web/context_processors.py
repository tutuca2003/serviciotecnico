from .models import DatosNegocio


def negocio(request):
    return {"negocio": DatosNegocio.obtener()}
