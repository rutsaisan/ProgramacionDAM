# -------------------------------------------------------------
# 🧰 Cómo instalar ttkbootstrap:
# Ejecuta en tu terminal o consola:
#     pip install ttkbootstrap
# -------------------------------------------------------------
# ttkbootstrap es una extensión de tkinter con temas modernos
# y widgets mejorados. Este programa la usa para crear una
# interfaz más profesional y visualmente atractiva.
# -------------------------------------------------------------

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import mysql.connector
from tkinter import messagebox


# --- Conexión con la base de datos ---
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="EmpresaDAM2526$",
    database="empresadam"
)
cursor = conexion.cursor()


# --- Función para insertar cliente ---
def insertar_cliente():
    dni = entry_dni.get().strip()
    nombre = entry_nombre.get().strip()
    apellidos = entry_apellidos.get().strip()
    email = entry_email.get().strip()

    if not dni or not nombre or not apellidos or not email:
        messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
        return

    try:
        cursor.execute("""
            INSERT INTO clientes (dni, nombre, apellidos, email)
            VALUES (%s, %s, %s, %s)
        """, (dni, nombre, apellidos, email))
        conexion.commit()
        messagebox.showinfo("Éxito", "Cliente insertado correctamente.")
        entry_dni.delete(0, END)
        entry_nombre.delete(0, END)
        entry_apellidos.delete(0, END)
        entry_email.delete(0, END)
        mostrar_clientes()  # Actualiza la tabla
    except mysql.connector.Error as err:
        messagebox.showerror("Error de base de datos", f"Ocurrió un error: {err}")


# --- Función para mostrar los clientes en la tabla ---
def mostrar_clientes():
    for fila in tabla.get_children():
        tabla.delete(fila)

    cursor.execute("SELECT id, dni, nombre, apellidos, email FROM clientes;")
    for fila in cursor.fetchall():
        tabla.insert("", END, values=fila)


# --- Ventana principal ---
ventana = ttk.Window(themename="flatly")  # Puedes probar otros temas: "superhero", "cyborg", "darkly", "morph"
ventana.title("Gestión de Clientes - EmpresaDAM")
ventana.geometry("750x500")

# --- Notebook (pestañas) ---
notebook = ttk.Notebook(ventana)
notebook.pack(fill=BOTH, expand=True, padx=10, pady=10)

# --- Pestaña 1: Insertar cliente ---
frame_insertar = ttk.Frame(notebook, padding=20)
notebook.add(frame_insertar, text="🧾 Insertar Cliente")

ttk.Label(frame_insertar, text="Introduce los datos del cliente:", font=("Segoe UI", 14, "bold")).pack(pady=10)

formulario = ttk.Frame(frame_insertar)
formulario.pack(pady=10)

# DNI/NIE
ttk.Label(formulario, text="DNI / NIE:", bootstyle="info").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_dni = ttk.Entry(formulario, width=40)
entry_dni.grid(row=0, column=1, pady=5)

# Nombre
ttk.Label(formulario, text="Nombre:", bootstyle="info").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_nombre = ttk.Entry(formulario, width=40)
entry_nombre.grid(row=1, column=1, pady=5)

# Apellidos
ttk.Label(formulario, text="Apellidos:", bootstyle="info").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_apellidos = ttk.Entry(formulario, width=40)
entry_apellidos.grid(row=2, column=1, pady=5)

# Email
ttk.Label(formulario, text="Email:", bootstyle="info").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_email = ttk.Entry(formulario, width=40)
entry_email.grid(row=3, column=1, pady=5)

# Botón insertar
ttk.Button(frame_insertar, text="💾 Insertar Cliente", bootstyle="success-outline", command=insertar_cliente).pack(pady=20)


# --- Pestaña 2: Ver clientes ---
frame_ver = ttk.Frame(notebook, padding=20)
notebook.add(frame_ver, text="📋 Ver Clientes")

ttk.Label
