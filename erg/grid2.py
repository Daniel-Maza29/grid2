#DANIEL RAFAEL MAZA RUIZ
import tkinter as tk
import tkinter.messagebox as messagebox

def registrar():
    info = f"nonbre: {entrada_nombre.get()}\napellido: {entrada_apellido.get()}\nEdad: {entrada_edad.get()}\ndireccion: {entrada_direccion.get()}\nnumero: {entrada_telefono.get()}\nSexo: {sexo.get()}\nCiudad: {ciudades[listbox_ciudad.curselection()[0]]}"
    messagebox.showinfo("Información del Registro", info)


ventana = tk.Tk()
ventana.title("Por favor llene el formulario")
ventana.geometry("400x400")


tk.Label(ventana, text="Nombres:").grid(row=0, column=0)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Apellidos:").grid(row=1, column=0)
entrada_apellido = tk.Entry(ventana)
entrada_apellido.grid(row=1, column=1)
#DANIEL RAFAEL MAZA RUIZ
tk.Label(ventana, text="Edad:").grid(row=2, column=0)
entrada_edad = tk.Entry(ventana)
entrada_edad.grid(row=2, column=1)

tk.Label(ventana, text="Dirección:").grid(row=3, column=0)
entrada_direccion = tk.Entry(ventana)
entrada_direccion.grid(row=3, column=1)

tk.Label(ventana, text="Teléfono celular:").grid(row=4, column=0)
entrada_telefono = tk.Entry(ventana)
entrada_telefono.grid(row=4, column=1)


sexo = tk.StringVar()
tk.Label(ventana, text="Genero con el que se identifica:").grid(row=5, column=0)
tk.Radiobutton(ventana, text="Masculino", variable=sexo, value="Masculino").grid(row=5, column=1)
tk.Radiobutton(ventana, text="Femenino", variable=sexo, value="Femenino").grid(row=5, column=2)


tk.Label(ventana, text="Ciudad en la que vive:").grid(row=6, column=0)
ciudades = ["Barranquilla", "Bógota", "Libano"]
listbox_ciudad = tk.Listbox(ventana, selectmode=tk.SINGLE, height=len(ciudades))
for ciudad in ciudades:
    listbox_ciudad.insert(tk.END, ciudad)
listbox_ciudad.grid(row=6, column=1)


tk.Button(ventana, text="Registrar", command=registrar).grid(row=7, column=0, columnspan=2)

ventana.mainloop()

#DANIEL RAFAEL MAZA RUIZ