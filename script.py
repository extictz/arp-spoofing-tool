import tkinter as tk
from tkinter import scrolledtext
from scapy.all import ARP, Ether, send, srp
import time
import threading
import uuid

# Advertencia
def advertencia():
    ventana_advertencia = tk.Toplevel()
    ventana_advertencia.title("Advertencia")
    label_advertencia = tk.Label(ventana_advertencia, text="Este tipo de ataque es ilegal y puede causar daños a la red y a los dispositivos conectados.")
    label_advertencia.pack()
    boton_aceptar = tk.Button(ventana_advertencia, text="Aceptar", command=ventana_advertencia.destroy)
    boton_aceptar.pack()

# Requerir autorización
def requerir_autorizacion():
    ventana_autorizacion = tk.Toplevel()
    ventana_autorizacion.title("Autorización")
    label_autorizacion = tk.Label(ventana_autorizacion, text="¿Estás seguro de que deseas ejecutar este ataque?")
    label_autorizacion.pack()
    boton_si = tk.Button(ventana_autorizacion, text="Sí", command= lambda: [ventana_autorizacion.destroy(), iniciar_spoofing()])
    boton_si.pack()
    boton_no = tk.Button(ventana_autorizacion, text="No", command=ventana-autorizacion.destroy)
    boton_no.pack()

# Limitar el alcance
def limitar_alcance(ip_objetivo):
    # Especifica un rango de IPs para atacar
    ip_rango = "192.168.223.0/24"
    if ip_objetivo in ip_rango:
        return True
    else:
        return False

# Agregar mecanismo de detención
def detener_spoofing():
    global ataque_en_curso
    ataque_en_curso = False

# Documentar el código
def obtener_mac(ip):
    """
     Obtiene la dirección MAC del dispositivo con la IP especificada.
     """
     # Código...

# ... (resto del código)

if __name__ == "__main__":
      # Creación del interfaz gráfico...
      advertencia_boton = tk.Button(ventana, text="Advertencia", command=advertencia)
      advertencia_boton.pack()
      autorizar_boton  -tk.Button-(Ventanacute.text-"Autorizar"-comandorequeri-/autoriizaclón-