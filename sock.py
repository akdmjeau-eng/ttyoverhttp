import socket
import sys

def conectar():
    # Asegúrate de que el servidor esté corriendo en estos datos:
    ip = "127.0.0.1"
    port = 4444

    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print(f"[*] Intentando conectar a {ip}:{port}...")
        c.connect((ip, port))
        print("[+] Conexión establecida con éxito.")
        return c
    except ConnectionRefusedError:
        print("[-] Error: Conexión rechazada. ¿Olvidaste iniciar el servidor?")
        sys.exit(1)
    except Exception as e:
        print(f"[-] Ocurrió un error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    conectar()
