# Cotizaciones App

Aplicación para comparar cotizaciones de múltiples proveedores, mostrando el mejor precio por ítem y generando un reporte Excel.

## Estructura

- **backend/**: API y procesamiento de archivos (Flask)
- **frontend_web/**: Interfaz web (Flask + HTML/CSS/JS)
- **data/**: Subidas temporales
- **output/**: Resultados exportados

---

## Instalación y ejecución local

```sh
cd backend
pip install -r requirements.txt
python app.py
```

## Despliegue en Azure

### 1. Requisitos previos

- Tener este repositorio en GitHub: https://github.com/gvlastel/cotizaciones-app

### 2. Opción A: Azure App Service (Linux) con Docker

1. Haz push de tu proyecto a GitHub.
2. En Azure Portal, crea un recurso "Web App" (Linux).
3. Elige "Implementación continua" desde GitHub (Deployment Center).
4. Selecciona el repo `gvlastel/cotizaciones-app` y elige la carpeta `/backend`.
5. Azure detectará el Dockerfile y desplegará automáticamente.
6. Tu app estará disponible en la URL de Azure.

### 3. Opción B: Azure App Service (Windows) tradicional

1. Usa el archivo `web.config` y asegúrate de que el archivo principal sea `app.py`.
2. Sube el contenido de `/backend` a Azure Web App.
3. Configura la variable de inicio (`gunicorn -w 4 -b 0.0.0.0:8000 app:app`).

---

## Uso Web

- Accede a la web en la URL asignada por Azure.
- Flujo:
  1. Bienvenida → Login
  2. Sube presupuesto del mandante
  3. Sube cotizaciones de proveedores (se activan progresivamente)
  4. Procesa y descarga resultados

---

## Soporte de archivos

- `.xls`, `.xlsx`, `.pdf`, `.csv`, `.txt`
- El presupuesto del mandante define los ítems a cotizar
- Las ofertas se activan progresivamente al subir archivos

---
