from napalm import get_network_driver

# Datos de autenticación
devices = [
    {
        "device_type": "iosxe",
        "hostname": "192.168.56.11",
        "username": "codingnetworks",
        "password": "Coding.Networks1",
    },
    {
        "device_type": "iosxe",
        "hostname": "192.168.56.15",
        "username": "codingnetworks",
        "password": "Coding.Networks1",
    },
]

# Itera a través de la lista de dispositivos
for device_info in devices:
    # Crea una instancia de NAPALM para el dispositivo
    driver = get_network_driver(device_info["device_type"])
    device = driver(
        hostname=device_info["hostname"],
        username=device_info["username"],
        password=device_info["password"],
    )

    try:
        # Conecta al dispositivo
        device.open()

        # Configurar la interfaz Loopback
        loopback_config = [
            "interface Loopback122",
            "description Interfaz Loopback con NAPALM",
            "ip address 192.168.122.1 255.255.255.255",
        ]

        # Aplicar la configuración
        device.load_merge_candidate(config="\n".join(loopback_config))
        device.commit_config()

    except Exception as e:
        print(f"Error al conectar con {device_info['hostname']}: {str(e)}")
    finally:
        # Cierra la conexión al dispositivo
        device.close()
