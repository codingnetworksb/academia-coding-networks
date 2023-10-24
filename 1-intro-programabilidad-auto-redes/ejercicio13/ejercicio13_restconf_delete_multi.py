import requests
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

# Elimina los Warnings que salen en consola
disable_warnings(InsecureRequestWarning)

devices = ["192.168.56.11", "192.168.56.15"]
# Datos de autenticación
username = "codingnetworks"
password = "Coding.Networks1"

# Encabezados HTTP
headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json",
}
for device in devices:
    for num in range(100, 130):
        interfaz = f"Loopback{num}"
        url = f"https://{device}/restconf/data/ietf-interfaces:interfaces/interface={interfaz}"

        # Enviar la solicitud HTTP DELETE para configurar la interfaz Loopback
        response = requests.delete(
            url,
            auth=HTTPBasicAuth(username, password),
            headers=headers,
            json={},
            verify=False,  # Desactivar la verificación de certificado (no recomendado en producción)
        )

        # Comprobamos el código de estado HTTP
        if response.status_code >= 200 and response.status_code < 300:
            # El código de estado está en el rango 200-299, lo que indica una respuesta exitosa.
            print(f"Dispositivo: {device} Interfaz {interfaz} eliminada con éxito.")
        else:
            # El código de estado está fuera del rango 200-299, lo que indica un error.
            print(
                f"Error en la configuración. Código de estado HTTP: {response.status_code}"
            )
