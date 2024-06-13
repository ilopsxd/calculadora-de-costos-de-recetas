import tkinter as tk
from tkinter import ttk, messagebox

# Diccionario de platos y sus recetas
platos = {
    "Ensalada": "Lechuga, tomate, zanahoria, cebolla, aderezo",
    "Pizza": "Harina, salsa de tomate, queso, jamón, champiñones",
    "Sopa": "Agua, pollo, zanahoria, papa, sal"
}

def mostrar_receta(event):
    plato_seleccionado = combo_platos.get()
    receta = platos.get(plato_seleccionado, "")
    label_receta.config(text=f"Receta: {receta}")

def agregar_ingrediente():
    ingrediente = entry_ingrediente.get()
    cantidad = entry_cantidad.get()
    costo = entry_costo.get()
    tipo = tipo_cantidad.get()

    if not ingrediente or not cantidad or not costo or not tipo:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    try:
        cantidad = float(cantidad)
        costo = float(costo)
    except ValueError:
        messagebox.showerror("Error", "Cantidad y costo deben ser números.")
        return

    if tipo == "kg":
        costo_por_unidad = (costo / cantidad) / 10
    else:
        costo_por_unidad = costo / cantidad

    resultados.append(costo_por_unidad)
    actualizar_lista_resultados()

    # Limpiar campos después de agregar el ingrediente
    entry_ingrediente.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_costo.delete(0, tk.END)

def actualizar_lista_resultados():
    lista_resultados.delete(0, tk.END)
    for idx, costo in enumerate(resultados, start=1):
        lista_resultados.insert(tk.END, f"Ingrediente {idx}: {costo:.2f}")

def calcular_total():
    total = sum(resultados)
    messagebox.showinfo("Total", f"El costo total es: {total:.2f}")

def limpiar_resultados():
    lista_resultados.delete(0, tk.END)
    resultados.clear()  # Limpiar la lista de resultados

# Crear la ventana principal
root = tk.Tk()
root.title("Menú de Platos")
root.geometry("600x600")

# Crear y ubicar los widgets
label_plato = tk.Label(root, text="Seleccione un plato:")
label_plato.pack(pady=10)

combo_platos = ttk.Combobox(root, values=list(platos.keys()))
combo_platos.pack(pady=10)
combo_platos.bind("<<ComboboxSelected>>", mostrar_receta)

label_receta = tk.Label(root, text="")
label_receta.pack(pady=10)

frame_ingrediente = tk.Frame(root)
frame_ingrediente.pack(pady=10)

label_ingrediente = tk.Label(frame_ingrediente, text="Ingrese el ingrediente:")
label_ingrediente.grid(row=0, column=0, padx=5, pady=5)

entry_ingrediente = tk.Entry(frame_ingrediente)
entry_ingrediente.grid(row=0, column=1, padx=5, pady=5)

label_cantidad = tk.Label(frame_ingrediente, text="Ingrese la cantidad:")
label_cantidad.grid(row=1, column=0, padx=5, pady=5)

entry_cantidad = tk.Entry(frame_ingrediente)
entry_cantidad.grid(row=1, column=1, padx=5, pady=5)

label_costo = tk.Label(frame_ingrediente, text="Ingrese el costo:")
label_costo.grid(row=2, column=0, padx=5, pady=5)

entry_costo = tk.Entry(frame_ingrediente)
entry_costo.grid(row=2, column=1, padx=5, pady=5)

tipo_cantidad = tk.StringVar(value="kg")
radio_kg = tk.Radiobutton(frame_ingrediente, text="Kilogramos", variable=tipo_cantidad, value="kg")
radio_unidad = tk.Radiobutton(frame_ingrediente, text="Unidades", variable=tipo_cantidad, value="unidad")
radio_kg.grid(row=3, column=0, pady=5)
radio_unidad.grid(row=3, column=1, pady=5)

boton_agregar = tk.Button(frame_ingrediente, text="Agregar Ingrediente", command=agregar_ingrediente)
boton_agregar.grid(row=4, column=0, columnspan=2, pady=10)

label_resultados = tk.Label(root, text="Resultados:")
label_resultados.pack(pady=10)

lista_resultados = tk.Listbox(root, height=5, width=60)
lista_resultados.pack(pady=10)

frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

boton_calcular = tk.Button(frame_botones, text="Calcular Total", command=calcular_total)
boton_calcular.pack(padx=10, pady=5, side=tk.LEFT)

boton_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar_resultados)
boton_limpiar.pack(padx=10, pady=5, side=tk.LEFT)

boton_salir = tk.Button(frame_botones, text="Salir", command=root.quit)
boton_salir.pack(padx=10, pady=5, side=tk.RIGHT)

# Lista para almacenar los resultados de cada ingrediente
resultados = []

# Iniciar el bucle principal de la interfaz
root.mainloop()