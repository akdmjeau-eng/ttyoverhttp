import socket
import sys
import os

def conectar():
    # CONFIGURACIÓN: Revisa que estas IPs sean correctas
    ip = "192.168.1.1" # Cambia esto por la IP real del servidor
    port = 4444

    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.settimeout(5) # No esperar eternamente

    try:
        print(f"[*] Buscando ruta hacia {ip}...")
        c.connect((ip, port))
        print(f"[+] Conexión exitosa a {ip}")
        return c
    except OSError as e:
        if e.errno == 113:
            print(f"[-] Error 113: No hay ruta al host ({ip}).")
            print("    Verifica que el dispositivo esté encendido y en la misma>
        else:
            print(f"[-] Error de red: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[-] Error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    conectar()
