import tkinter as tk
from tkinter import ttk

from tkinter import filedialog
import os
import shutil


class MiAplicacion:
    def __init__(self, master):
        master.resizable(False, False)
        self.master = master
        master.title("Aplicacion de BUSQUEDA DE ARCHIVOS")
        master.geometry("400x400")
       

        self.etiqueta = tk.Label(master, text="Esto es un progrma de pruebas para mover o copiar archivos,\n puede tener errorres", font=("Arial", 11),  width=50, height=10)
        self.etiqueta.pack(pady=20)

        self.boton = tk.Button(master, text="Lo entiendo pero me quiero arriesgar", command=self.cambiar_contenido)
        self.boton.pack(pady=20)

    def cambiar_contenido(self):
        # Borrar todos los widgets en la ventana actual
        for widget in self.master.winfo_children():
            widget.destroy()
        
        # Crear nuevos widgets o actualizar la interfaz gráfica según tus necesidades
        self.etiqueta = tk.Label(self.master, text="Escribe aqui lo que quieres buscar")
        self.etiqueta.pack()
        self.text_box = tk.Text(self.master, height=10, width=40,wrap=tk.WORD)
        self.text_box.pack()

        #crear boton para seleccionar directorio donde buscar
        self.boton_seleccionar_busqueda = tk.Button(self.master, text="Seleccionar Directorio Donde Buscar", command=lambda: self.seleccionar_directorio(1))
        self.boton_seleccionar_busqueda.pack()

        self.directorio_seleccionado = ""

        self.directiorio = tk.Label(self.master, text="Directorio seleccionado: " )
        self.directiorio.pack()

        # Crea un nuevo marco para los botones de radio
        frame_radio = tk.Frame(self.master)
        frame_radio.pack()

        # Crea radio buttons para seleccionar si se mueve o copia
        self.opcion_seleccionada = tk.StringVar()
        self.radio_btn1 = tk.Radiobutton(frame_radio, text="Mover", variable=self.opcion_seleccionada, value="opcion1")
        self.radio_btn1.grid(row=0, column=0)
        self.radio_btn2 = tk.Radiobutton(frame_radio, text="Copiar", variable=self.opcion_seleccionada, value="opcion2")
        self.radio_btn2.grid(row=0, column=1)

        #crear boton para seleccionar directorio donde se moveran o copiaran los archivos
        self.boton_seleccionar_destino = tk.Button(self.master, text="Seleccionar Directorio Destino", command=lambda: self.seleccionar_directorio(2))
        self.boton_seleccionar_destino.pack()
        self.directorio_destino_seleccionado = ""

        self.directiorio_destino = tk.Label(self.master, text="Directorio  destino seleccionado: " )
        self.directiorio_destino.pack()

        #crear boton para ejecutar el programa
        nuevo_boton = tk.Button(self.master, text="Buscar", command=self.volver)
        nuevo_boton.pack()


    def seleccionar_directorio(self, numero_directorio):
        # Abrir el cuadro de diálogo para seleccionar un directorio
        directorio_seleccionado = filedialog.askdirectory()
        def truncate_string(s):
            if len(s) > 30:
                return '...' + s[-20:]
            else:
                return s

        if numero_directorio == 1:
            self.directorio_seleccionado = directorio_seleccionado
            self.directorio_seleccionado = truncate_string(self.directorio_seleccionado)
            self.directiorio.config(text="Directorio seleccionado: " + self.directorio_seleccionado)
            self.directiorio.pack()

        elif numero_directorio == 2:
            self.directorio_destino_seleccionado = directorio_seleccionado
            self.directorio_destino_seleccionado = truncate_string(self.directorio_destino_seleccionado)
            self.directiorio_destino.config(text="Directorio  destino seleccionado: " + self.directorio_destino_seleccionado)
            self.directiorio_destino.pack()

    def volver(self):
        # ejecutar el programa
       if self.directorio_seleccionado != "" and self.directorio_destino_seleccionado != "" and self.opcion_seleccionada.get() != "" and self.text_box.get("1.0", "end-1c") != "":
            if self.opcion_seleccionada.get() == "opcion1":
                self.mover_archivos(self.directorio_seleccionado, self.directorio_destino_seleccionado, self.text_box.get("1.0", "end-1c"))
            elif self.opcion_seleccionada.get() == "opcion2":
                self.copiar_archivos(self.directorio_seleccionado, self.directorio_destino_seleccionado, self.text_box.get("1.0", "end-1c"))
    
    def mover_archivos(self, origen, destino, nombres_archivos):
        # Verificar si el directorio de destino existe, si no, crearlo
        if not os.path.exists(destino):
            os.makedirs(destino)
        # iterar sobre la lista de nombres de archivos separados por saltos de linea
        for nombre_archivo in nombres_archivos.split("\n"):
            if nombre_archivo != "":    
                # Iterar sobre los archivos en el directorio de origen
                for archivo in os.listdir(origen):
                    if archivo.endswith(nombre_archivo+".pdf"):
                        origen_path = os.path.join(origen, archivo)
                        destino_path = os.path.join(destino, archivo)
                
                    # Mover el archivo al directorio de destino
                        shutil.move(origen_path, destino_path)


        
        
    def copiar_archivos(self, origen, destino, nombres_archivos):
        # Verificar si el directorio de destino existe, si no, crearlo
        if not os.path.exists(destino):
            os.makedirs(destino)
        # iterar sobre la lista de nombres de archivos separados por saltos de linea
        for nombre_archivo in nombres_archivos.split("\n"):
            if nombre_archivo != "":    
                # Iterar sobre los archivos en el directorio de origen
                for archivo in os.listdir(origen):
                    if archivo.endswith(nombre_archivo+".pdf"):
                        origen_path = os.path.join(origen, archivo)
                        destino_path = os.path.join(destino, archivo)
                
                        # Copiar el archivo al directorio de destino
                        shutil.copy(origen_path, destino_path)
       
             

    
   
            
          

root = tk.Tk()
app = MiAplicacion(root)
root.mainloop()