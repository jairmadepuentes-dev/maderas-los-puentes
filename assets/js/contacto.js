document.addEventListener('DOMContentLoaded', () => {
  const formulario = document.getElementById('formulario-cotizacion');

  if (!formulario) return;

  formulario.addEventListener('submit', (evento) => {
    evento.preventDefault();

    const datos = new FormData(formulario);
    const mensaje = [
      'Hola, quiero solicitar una cotización desde la página web.',
      '',
      `Nombre: ${datos.get('nombre')}`,
      `Correo: ${datos.get('correo')}`,
      `Teléfono: ${datos.get('telefono')}`,
      `Solicitud: ${datos.get('tipo')}`,
      `Mensaje: ${datos.get('mensaje')}`
    ].join('\n');

    if (typeof window.gtag === 'function') {
      window.gtag('event', 'envio_formulario_whatsapp', {
        event_category: 'whatsapp',
        event_label: 'formulario_contacto'
      });
    }

    window.open(`https://wa.me/573108068408?text=${encodeURIComponent(mensaje)}`, '_blank', 'noopener');
  });
});
