# Página del servicio técnico

## Probarla en tu computadora

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Página: http://127.0.0.1:8000/
- Panel de administración: http://127.0.0.1:8000/admin/

En el panel puedes cambiar sin tocar código:
- **Datos del negocio**: nombre, teléfono, WhatsApp, correo, dirección, horario y enlace de Google Maps.
- **Servicios**: agregar, editar, ordenar u ocultar las tarjetas de servicios.
- **Mensajes de contacto**: lo que la gente envía desde el formulario. Marca "atendido" cuando respondas.

## Subirla gratis a PythonAnywhere

1. Crea una cuenta gratuita ("Beginner") en https://www.pythonanywhere.com/.
   Tu página quedará en `https://TUUSUARIO.pythonanywhere.com`.
2. En la pestaña **Files**, sube el archivo `serviciotecnico.zip`.
3. Abre una consola **Bash** (pestaña Consoles) y ejecuta:

   ```bash
   unzip serviciotecnico.zip
   cd serviciotecnico
   mkvirtualenv --python=python3.13 sitio
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   ```

   Si `python3.13` no está disponible, usa la versión más nueva que aparezca (3.12, 3.11...).

4. Ve a la pestaña **Web** → **Add a new web app** → **Manual configuration** → elige la misma versión de Python.
5. En esa pestaña Web configura:
   - **Virtualenv**: `/home/TUUSUARIO/.virtualenvs/sitio`
   - **Static files**: URL `/static/` → Directory `/home/TUUSUARIO/serviciotecnico/staticfiles`
6. Haz clic en el enlace del **WSGI configuration file**, borra todo su contenido y pega esto (cambia TUUSUARIO y la clave):

   ```python
   import os
   import sys

   path = "/home/TUUSUARIO/serviciotecnico"
   if path not in sys.path:
       sys.path.insert(0, path)

   os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"
   os.environ["DJANGO_DEBUG"] = "0"
   os.environ["DJANGO_ALLOWED_HOSTS"] = "TUUSUARIO.pythonanywhere.com"
   os.environ["DJANGO_SECRET_KEY"] = "PEGA-AQUI-UNA-CLAVE-LARGA-Y-ALEATORIA"

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

   Para generar una clave, en la consola Bash ejecuta:
   `python -c "import secrets; print(secrets.token_urlsafe(50))"`

7. De vuelta en la consola Bash:

   ```bash
   cd ~/serviciotecnico
   python manage.py collectstatic --noinput
   ```

8. En la pestaña **Web**, pulsa **Reload**. ¡Listo!
9. Entra a `https://TUUSUARIO.pythonanywhere.com/admin/` y completa los **Datos del negocio**.

**Importante:** en la cuenta gratuita la página se desactiva si no la renuevas. Entra a la pestaña
**Web** al menos una vez al mes y pulsa el botón para extenderla.

## Cuando hagas cambios

Sube los archivos modificados y ejecuta en la consola:

```bash
workon sitio
cd ~/serviciotecnico
python manage.py migrate
python manage.py collectstatic --noinput
```

Después pulsa **Reload** en la pestaña Web.

