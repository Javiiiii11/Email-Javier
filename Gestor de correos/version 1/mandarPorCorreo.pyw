import os
import smtplib
from email.message import EmailMessage
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# Dirección de correo del destinatario
DESTINATARIO_EMAIL = "" # Rellenar con correo del destinatario

def seleccionar_archivos():
    archivos = filedialog.askopenfilenames(initialdir=os.getcwd(), title="Seleccionar Archivos")
    return archivos

def enviar_correo(archivos, asunto):
    try:
        remitente_email = "" # Rellenar con tu correo
        remitente_password = "" # Rellenar con la contraseña de aplicacion del correo
        
        msg = EmailMessage()
        msg['Subject'] = asunto
        msg['From'] = remitente_email
        msg['To'] = DESTINATARIO_EMAIL
        
        for archivo in archivos:
            with open(archivo, 'rb') as f:
                datos_archivo = f.read()
                nombre_archivo = os.path.basename(archivo)
                msg.add_attachment(datos_archivo, maintype='application', subtype='octet-stream', filename=nombre_archivo)
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
            servidor.login(remitente_email, remitente_password)
            servidor.send_message(msg)
        
        messagebox.showinfo("Éxito", "¡Correo enviado con éxito!")
    
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al enviar el correo: {str(e)}")

def menu_principal():
    root = tk.Tk()
    root.withdraw()
    
    respuesta = messagebox.askyesno("Inicio", "¿Deseas enviar archivos por correo?")
    if respuesta:
        archivos = seleccionar_archivos()
        if not archivos:
            messagebox.showwarning("Advertencia", "¡No se seleccionaron archivos!")
            return
        
        asunto = simpledialog.askstring("Asunto", "Introduce el asunto del correo:")
        
        if asunto:
            enviar_correo(archivos, asunto)
        else:
            messagebox.showwarning("Advertencia", "¡Falta el asunto del correo!")

if __name__ == "__main__":
    menu_principal()
