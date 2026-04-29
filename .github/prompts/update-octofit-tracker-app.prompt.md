mode: 'agent'
model: GPT-4.1

# Actualizaciones de la aplicación Django

- Todos los archivos del proyecto Django están en el directorio `octofit-tracker/backend/octofit_tracker`.

1. Actualizar `settings.py` para la conexión con MongoDB y CORS.
2. Actualizar `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py` y `admin.py` para soportar las colecciones de usuarios, equipos, actividades, tabla de clasificación y entrenamientos.
3. Asegurarse de que `/` apunte a la API y que `api_root` esté presente en `urls.py`.
