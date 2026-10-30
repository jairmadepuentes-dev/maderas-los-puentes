# Maderas Los Puentes

Sitio web estático preparado para publicación en GitHub Pages con el dominio `maderaslospuentes.com`.

## Publicación

1. Subir el contenido de esta carpeta a la rama `main` del repositorio definitivo.
2. En GitHub, abrir **Settings → Pages**.
3. Publicar desde **Deploy from a branch**, rama `main`, carpeta `/ (root)`.
4. Confirmar que el dominio personalizado sea `maderaslospuentes.com` y que **Enforce HTTPS** esté activo cuando GitHub lo permita.

Los archivos `CNAME`, `.nojekyll`, `robots.txt` y `sitemap.xml` deben permanecer en la raíz.

## Prueba local

Desde esta carpeta, ejecutar:

```bash
python3 -m http.server 8085 --bind 127.0.0.1
```

Abrir `http://127.0.0.1:8085`. El formulario de contacto valida los campos obligatorios, prepara la solicitud y abre WhatsApp; no envía correos electrónicos y no necesita servidor ni base de datos.

## Actualización del catálogo

El catálogo está dentro de `productos.html`. Las fotografías publicadas están en `assets/images/productos/`. Antes de reemplazar una imagen, conservar exactamente su nombre de archivo.

## Datos que conviene verificar antes de publicar

- Teléfonos, correo, dirección y horarios.
- Productos, medidas, impuestos y fotografías.
- Identificador de Google Analytics `G-JPG8V5E4BZ`.
- Titularidad del dominio y configuración de GitHub Pages.

## Dependencias externas de la portada

La portada conserva temporalmente componentes de la versión adaptada de GoDaddy para no alterar su diseño ni comportamiento:

- hojas tipográficas y scripts cargados desde `img1.wsimg.com`;
- funcionamiento de la galería, mapa y horarios asociado a esos scripts;
- cinco imágenes de stock o iStock que permanecen enlazadas de forma externa y no están incluidas en esta entrega: `isteam/stock/19437`, `iStock-106423936-scaled.jpg`, `isteam/stock/103895`, `isteam/stock/nyqObaA` e `isteam/stock/98275`.

Las fotografías propias autorizadas de Maderas Los Puentes utilizadas directamente por la portada tienen copias locales idénticas en `assets/images/portada/`. La galería heredada todavía obtiene sus imágenes mediante el componente externo de GoDaddy.

Si GoDaddy retira o restringe esos recursos, la portada puede perder tipografías, galería, mapa, horarios o imágenes de stock. Su sustitución completa requiere una implementación propia y la confirmación de licencias de las cinco imágenes de stock; no debe hacerse como un cambio rutinario de contenido.

En pruebas locales, el componente heredado solicita `/markup/ad` y recibe un error 404; es un anuncio de GoDaddy y no una función comercial del sitio. El script de telemetría `scc-c2` también puede ser rechazado por GoDaddy. No se deben crear archivos ficticios para ocultar esos avisos. La referencia obsoleta a `/sw.js` fue retirada porque no existía un *service worker* ni una función asociada.

Google Analytics está configurado con el identificador `G-JPG8V5E4BZ`. Confirmar visitas y eventos reales requiere acceso a la propiedad correspondiente de Google Analytics.
