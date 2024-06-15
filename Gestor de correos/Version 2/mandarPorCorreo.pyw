import os
import smtplib
from email.message import EmailMessage
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# Dirección de correo del destinatario
DESTINATARIO_EMAIL = "" # Rellenar con correo del destinatario

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(initialdir=os.getcwd(), title="Seleccionar Archivo")
    return archivo

def enviar_correo(archivo, asunto, descripcion):
    try:
        remitente_email = "" # Rellenar con tu correo
        remitente_password = "" # Rellenar con la contraseña de aplicacion del correo
        
        msg = EmailMessage()
        msg['Subject'] = asunto
        msg['From'] = remitente_email
        msg['To'] = DESTINATARIO_EMAIL
        
        # Construir el contenido del correo
        contenido_correo = descripcion.strip()
        if contenido_correo:
            contenido_correo += "\n\n"
        contenido_correo += "Mensaje enviado desde @javier correos"
        msg.set_content(contenido_correo)
        
        if archivo:
            with open(archivo, 'rb') as f:
                datos_archivo = f.read()
                nombre_archivo = os.path.basename(archivo)
                msg.add_attachment(datos_archivo, maintype='application', subtype='octet-stream', filename=nombre_archivo)
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
            servidor.login(remitente_email, remitente_password)
            servidor.send_message(msg)
        
        messagebox.showinfo("@javier - Éxito", "¡Correo enviado con éxito!")
    
    except Exception as e:
        messagebox.showerror("@javier - Error", f"Fallo al enviar el correo: {str(e)}")

def redimensionar_imagen(ruta, width, height):
    imagen = tk.PhotoImage(file=ruta)
    imagen_redimensionada = imagen.subsample(2)  # Ajusta el tamaño según sea necesario
    return imagen_redimensionada

def menu_principal():
    root = tk.Tk()
    root.title("@javier - Reenviarme correos")
    
    # Configurar el tamaño y la posición de la ventana en el centro de la pantalla
    window_width = 1000
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # Cambiar el color de fondo
    root.configure(bg="#333344")
    
    def enviar():
        archivo = archivo_var.get()
        asunto = asunto_var.get()
        descripcion = descripcion_text.get("1.0", tk.END).strip()
        
        # Si no se ha especificado asunto, poner un asunto predeterminado
        if not asunto:
            asunto = "Asunto no especificado"
        
        # Añadir el mensaje automático solo si hay descripción
        if descripcion:
            descripcion += f"\n\nMensaje enviado desde @javier correos"
        
        if not archivo:
            messagebox.showwarning("@javier - Advertencia", "¡No se ha seleccionado ningún archivo!")
            return
        
        enviar_correo(archivo, asunto, descripcion)
    
    def seleccionar_archivo_callback():
        archivo = seleccionar_archivo()
        if archivo:
            archivo_var.set(archivo)
            entry_archivo.config(state='normal')
            entry_archivo.delete(0, tk.END)
            entry_archivo.insert(0, archivo)
            entry_archivo.config(state='readonly')
    
    # Crear un marco para la imagen a la derecha
    frame_imagen = tk.Frame(root, bg="#333344")
    frame_imagen.grid(row=1, column=2, rowspan=4, padx=20, pady=10)
    
    # Ruta a tu imagen y redimensionamiento
    ruta_logo = 'logo.png'
    imagen_redimensionada = redimensionar_imagen(ruta_logo, width=100, height=100)
    
    # Mostrar la imagen redimensionada
    label_imagen = tk.Label(frame_imagen, image=imagen_redimensionada, bg="#333344")
    label_imagen.image = imagen_redimensionada  # Mantener una referencia
    label_imagen.pack(pady=10)
    
    # Estilos para las tipografías
    estilo_calibri = ("Calibri", 11)
    estilo_rockwell = ("Rockwell Extra Bold", 14)
    
    tk.Label(root, text="Asunto:", bg="#333344", fg="white", font=estilo_rockwell).grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
    asunto_var = tk.StringVar()
    entry_asunto = tk.Entry(root, textvariable=asunto_var, width=67, font=estilo_calibri)
    entry_asunto.grid(row=1, column=1, padx=10, pady=30)
    
    tk.Label(root, text="Descripción:", bg="#333344", fg="white", font=estilo_rockwell).grid(row=2, column=0, sticky=tk.NW, padx=10, pady=5)
    descripcion_text = tk.Text(root, width=50, height=10, font=estilo_calibri)
    descripcion_text.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Label(root, text="Archivo:", bg="#333344", fg="white", font=estilo_rockwell).grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
    archivo_var = tk.StringVar()
    entry_archivo = tk.Entry(root, textvariable=archivo_var, width=68, state='readonly', font=estilo_calibri)
    entry_archivo.grid(row=4, column=1, padx=10, pady=5)
    
    tk.Button(root, text="Seleccionar Archivo", command=seleccionar_archivo_callback, bg="#555577", fg="white", font=estilo_calibri).grid(row=4, column=2, padx=10, pady=5)
    tk.Button(root, text="Enviar", command=enviar, bg="#555577", fg="white", font=estilo_calibri).grid(row=5, column=1, padx=10, pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    menu_principal()
