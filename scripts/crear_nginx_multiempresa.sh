#!/bin/bash

# Ruta de la plantilla Nginx dentro del proyecto
TEMPLATE="/home/odoo-crystal/odoo-18-docker/nginx_templates/crystalitservice.com"

# Solicita el dominio
read -p "👉 Ingresa el nuevo dominio (ej: empresa1.com): " dominio
dominio_www="www.${dominio}"
archivo="/etc/nginx/sites-available/${dominio}"

# Verifica que la plantilla exista
if [ ! -f "$TEMPLATE" ]; then
  echo "❌ No se encontró la plantilla base en: $TEMPLATE"
  exit 1
fi

# Copiar la plantilla al archivo destino
cp "$TEMPLATE" "$archivo"

# Reemplazar los dominios en el nuevo archivo
sed -i "s/www\.crystalitservice\.com/${dominio_www}/g" "$archivo"
sed -i "s/crystalitservice\.com/${dominio}/g" "$archivo"

# Crear enlace simbólico
if [ ! -L "/etc/nginx/sites-enabled/${dominio}" ]; then
  ln -s "$archivo" /etc/nginx/sites-enabled/
fi

# Verificar configuración de Nginx
echo "🔍 Verificando configuración de Nginx..."
nginx -t 2>&1 | tee /tmp/nginx_test.log
if [ "${PIPESTATUS[0]}" -ne 0 ]; then
  echo "❌ Error al verificar configuración Nginx:"
  echo "----------------------------------------"
  cat /tmp/nginx_test.log
  echo "----------------------------------------"
  echo "💡 Revisa el archivo generado: $archivo"
  exit 1
fi

# Recargar Nginx
echo "🔄 Recargando Nginx..."
if ! systemctl reload nginx; then
  echo "❌ Error al recargar Nginx."
  exit 1
fi

# Ejecutar Certbot para HTTPS
echo "🔒 Solicitando certificado SSL para $dominio y $dominio_www..."
certbot --nginx -d "$dominio" -d "$dominio_www"
if [ $? -ne 0 ]; then
  echo "❌ Certbot falló. Revisa el log en /var/log/letsencrypt/letsencrypt.log"
  exit 1
fi

echo "✅ Listo. El dominio https://${dominio_www} está configurado correctamente."

