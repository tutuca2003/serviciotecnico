from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactoForm
from .models import Servicio


def inicio(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "¡Gracias! Recibimos tu mensaje y te contactaremos pronto."
            )
            return redirect("/#contacto")
    else:
        form = ContactoForm()

    return render(
        request,
        "web/inicio.html",
        {"servicios": Servicio.objects.filter(activo=True), "form": form},
    )
